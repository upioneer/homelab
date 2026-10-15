# Indra OCR

[Indra OCR](https://github.com/datalab-to/indra) is an ultra-fast, CPU-optimized document intelligence and OCR engine created by [Datalab](https://www.datalab.to/blog/indra-ocr). Built on ONNX Runtime without requiring a GPU or PyTorch, Indra OCR utilizes a 1-million-parameter recognition model to read documents and convert PDFs or scanned images into structured Markdown, plain text, or detailed JSON.

## Key Features

- **Extreme CPU Throughput**: Processes up to ~49 pages per second across multi-core CPUs (~230 ms latency per page on 4 x86 cores), running 11–17x faster than Tesseract or PaddleOCR.
- **Layout & Block Analysis**: Provides bounding boxes for every detected line and layout block (headings, lists, tables, captions, footnotes, and headers/footers) with reading order extraction.
- **Digital PDF Acceleration**: Intelligently inspects the PDF's native text layer across any script, applying OCR only to missing text elements or embedded images.
- **LaTeX Math Detection**: Optional `--math` mode detects mathematical equations and formats them as inline/block LaTeX (`$...$`).
- **Interactive Web Viewer**: Built-in visual inspector allows dragging and dropping PDFs or images to inspect bounding boxes, reading order, and Markdown side-by-side.
- **Lightweight Footprint**: Model weights total only ~18 MB and download automatically from Hugging Face.

## Configuration & Environment Variables

This deployment uses a [`.env`](.env) file in the same directory to manage port bindings and Hugging Face authentication tokens.

> [!IMPORTANT]
> **Credentials & Configuration Awareness**
>
> A [`.env`](.env) file is provided in this directory. Review and configure the following variables before deployment:
> - `INDRA_PORT`: Host port exposed for the interactive web viewer (defaults to `8765`).
> - `HF_TOKEN`: *(Optional)* Your personal Hugging Face API token. While the model weights are public, providing a token helps prevent rate limits during initial model download or if deploying behind an enterprise firewall.

## Deployment Instructions

To deploy Indra OCR with Docker Compose:

1. Navigate to this directory:
   ```bash
   cd Indra-OCR
   ```

2. *(Optional)* Review or adjust settings in the [`.env`](.env) file:
   ```bash
   nano .env
   ```

3. Build the container image and launch in detached mode:
   ```bash
   docker compose up -d --build
   ```

4. Access the interactive web viewer in your browser:
   ```
   http://<host-ip>:8765
   ```

### Command Line Batch Processing

You can also use Indra OCR directly for CLI batch jobs inside the running container or on files mounted to `./data`:

```bash
# Convert a PDF to Markdown printed to stdout
docker compose exec indra-ocr indra-ocr /data/document.pdf

# Convert all PDFs in ./data to Markdown files using all CPU cores
docker compose exec indra-ocr indra-ocr /data/*.pdf --out /data/results/

# Extract full JSON metadata (bounding boxes, layout labels, confidence scores)
docker compose exec indra-ocr indra-ocr /data/scan.png --format json

# Enable inline LaTeX math extraction
docker compose exec indra-ocr indra-ocr /data/paper.pdf --math
```

### Managing the Container

```bash
# View live container logs
docker compose logs -f

# Check container status
docker compose ps

# Stop the container
docker compose down
```

## Docker Compose File

The companion Compose file is available at [docker-compose.yml](docker-compose.yml):

```yaml
services:
  indra-ocr:
    build: .
    container_name: indra-ocr
    restart: unless-stopped
    ports:
      - "${INDRA_PORT:-8765}:8765"
    volumes:
      - ./data:/data
      - indra_cache:/root/.cache/huggingface
    environment:
      - HF_TOKEN=${HF_TOKEN:-}
      - INDRA_PORT=8765

volumes:
  indra_cache:
    driver: local
```
