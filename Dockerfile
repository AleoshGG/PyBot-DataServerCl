# /api_usuarios/Dockerfile

# Usar una imagen base ligera de Python
FROM python:3.10-slim
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de tu API
COPY . .

# Exponer el puerto que usará Gunicorn (el mismo que en el docker-compose)
EXPOSE 8000

# --- Comando de arranque ---
# Le decimos a Gunicorn que escuche en todos lados (0.0.0.0) en el puerto 8000
# y que sirva la variable 'app' que está en el archivo 'main.py'
#
# !! Ajusta 'main:app' si tu archivo se llama diferente (ej. 'app:app') !!
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]