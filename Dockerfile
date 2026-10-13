# Imagen base ligera
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY src/ ./src/
COPY config/ ./config/
COPY examples/ ./examples/

# Ejecutar como usuario sin privilegios
RUN useradd --create-home monitor
USER monitor

# Comando por defecto
ENTRYPOINT ["python3", "-m", "src.main"]
