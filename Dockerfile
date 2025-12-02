FROM python:3.12-slim

# Install system dependencies (FFmpeg + others)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install python libs
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Django collectstatic (optional)
RUN python manage.py collectstatic --noinput || true

# Run server
CMD ["gunicorn", "karaoke_project.wsgi:application", "--bind", "0.0.0.0:8000"]
