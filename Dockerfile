# Build image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy requirements
COPY app/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ /app/

# Run with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:2000", "main:app"]
