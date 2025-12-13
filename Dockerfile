# Python image for running the FEC ingesters
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (git for VCS deps like ipython-sql, libpq for psycopg2)
RUN apt-get update \
     && apt-get install -y --no-install-recommends \
         git \
         build-essential \
         libpq-dev \
     && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default environment mode inside container (overridable)
ENV ENV_MODE=prod

# Ensure entrypoint script is executable
RUN chmod +x /app/docker-entrypoint.sh

# Run migrations then the ingestion pipeline
ENTRYPOINT ["/app/docker-entrypoint.sh"]
