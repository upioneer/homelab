FROM python:3.11-slim

# Install system dependencies for OpenCV and pypdfium2 rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install indra-ocr
RUN pip install --no-cache-dir indra-ocr

# Copy custom entrypoint for container network binding
COPY entrypoint.py /app/entrypoint.py
RUN chmod +x /app/entrypoint.py

# Create directory for documents and model cache
RUN mkdir -p /data /root/.cache/huggingface

EXPOSE 8765

ENV PYTHONUNBUFFERED=1

CMD ["python3", "/app/entrypoint.py", "--port", "8765"]
