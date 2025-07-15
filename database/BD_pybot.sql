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

select * FROM users;