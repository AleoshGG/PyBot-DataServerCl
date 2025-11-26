CREATE TABLE IF NOT EXISTS users (
    user_id    SERIAL PRIMARY KEY,
    first_name VARCHAR(45) NOT NULL,
    last_name  VARCHAR(45) NOT NULL,
    email      VARCHAR(50) NOT NULL UNIQUE,
    password   VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS prototypes (
    prototype_id   VARCHAR(100) PRIMARY KEY, 
    prototype_name VARCHAR(45) NOT NULL,
    model          VARCHAR(45) NOT NULL,
    user_id        INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sensors (
    sensor_id   SERIAL PRIMARY KEY,
    sensor_type VARCHAR(45) NOT NULL,
    model       VARCHAR(45) NOT NULL,
    prototype_id VARCHAR(100) NOT NULL,
    FOREIGN KEY (prototype_id) REFERENCES prototypes(prototype_id) ON DELETE CASCADE
); 

CREATE TABLE IF NOT EXISTS ids (
	generated_id VARCHAR(100) PRIMARY KEY
);

-- ALTER TABLE ids 
-- ALTER COLUMN generated_id TYPE VARCHAR(100); 

select * FROM ids;

-- select * FROM prototypes;

-- delete FROM users;

ALTER TABLE work_periods
ADD COLUMN backup BOOLEAN NOT NULL;


CREATE TABLE IF NOT EXISTS work_periods (
    period_id    SERIAL PRIMARY KEY,
    start_hour   TIMESTAMPTZ NOT NULL,
    end_hour     TIMESTAMPTZ NOT NULL,
    day_work     VARCHAR(15) NOT NULL,
    prototype_id VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS readings (
    period_id         SERIAL PRIMARY KEY,
    distance_traveled DECIMAL(10,4) NOT NULL,
    weight_waste      DECIMAL(10,4) NOT NULL,
    FOREIGN KEY (period_id) REFERENCES work_periods(period_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS waste_types (
    waste_id   SERIAL PRIMARY KEY,
    waste_type VARCHAR(50) NOT NULL
); 

CREATE TABLE IF NOT EXISTS waste_collection (
    waste_collection_id     INTEGER PRIMARY KEY DEFAULT 0,
    period_id   INTEGER NOT NULL,
    amount      INTEGER NOT NULL,
    waste_id    INTEGER NOT NULL,
    FOREIGN KEY (waste_id) REFERENCES waste_types(waste_id) ON DELETE CASCADE,
    FOREIGN KEY (period_id) REFERENCES readings(period_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS weight_data (
    weight_data_id     SERIAL PRIMARY KEY,
    period_id   INTEGER NOT NULL,
    hour_period TIMESTAMPTZ,
    weight      DECIMAL(10,4),
    FOREIGN KEY (period_id) REFERENCES readings(period_id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS gps_data (
    gps_data_id     SERIAL PRIMARY KEY,
    period_id   INTEGER NOT NULL,
    latitude    DECIMAL(11,8),
    longitude   DECIMAL(11,8),
    altitude    DECIMAL(10,4),
    speed       DECIMAL(8,4),
    date_gps    DATE,
    hour_UTC    TIMESTAMPTZ,
    FOREIGN KEY (period_id) REFERENCES readings(period_id) ON DELETE CASCADE
);


-- FUNCTIONS

-- FUNCION PARA OBTENER EL LA ULTIMA HORA REGISTRADA Y TOMARLO COMO EL FINAL DEL PERIODO PASADO
CREATE OR REPLACE FUNCTION getLastHourPeriod()
RETURNS TABLE (
    period_id INTEGER,
    hour_period TIMESTAMPTZ
    ) 
    LANGUAGE SQL
    STABLE
AS $$
    SELECT period_id, hour_period 
    FROM weight_data
    ORDER BY hour_period DESC
    LIMIT 1;
$$; 

-- FUNCION PARA DEVOLVER EL ULTIMO PESO REGISTRADO DE LA TABLA
CREATE OR REPLACE FUNCTION getLastWeight()
RETURNS DECIMAL(10,4)
LANGUAGE SQL
STABLE
AS $$
    SELECT weight
    FROM weight_data
    ORDER BY hour_period DESC
    LIMIT 1;
$$;

-- FUNCION PARA CALCULAR LA DISTANCIA TOTAL RECORRIDA Y RETORNARLA
CREATE OR REPLACE FUNCTION calcular_distancia_total(p_period INTEGER)
RETURNS NUMERIC(12,4)
LANGUAGE plpgsql
STABLE
AS $$
DECLARE
  total_dist NUMERIC := 0;
BEGIN
  WITH pares AS (
    SELECT
      latitude  AS lat2,
      longitude AS lon2,
      LAG(latitude ) OVER w AS lat1,
      LAG(longitude) OVER w AS lon1
    FROM gps_data
    WHERE period_id = p_period
    WINDOW w AS (ORDER BY date_gps, hour_UTC)
  )
  SELECT
    SUM(
      -- Fórmula de Haversine
      2 * 6371
      * ASIN(
          SQRT(
            POWER(SIN(RADIANS((lat2 - lat1) / 2)), 2)
            + COS(RADIANS(lat1))
              * COS(RADIANS(lat2))
              * POWER(SIN(RADIANS((lon2 - lon1) / 2)), 2)
          )
        )
    )
  INTO total_dist
  FROM pares
  WHERE lat1 IS NOT NULL AND lon1 IS NOT NULL;

  RETURN total_dist;
END;
$$;

-- INSERTS
INSERT INTO waste_types (waste_id, waste_type) VALUES (1, 'PET');
INSERT INTO waste_types (waste_id, waste_type) VALUES (2, 'CANS');