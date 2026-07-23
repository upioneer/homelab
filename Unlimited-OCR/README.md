# Unlimited-OCR

Unlimited OCR Works is an open-source parsing model from Baidu that aims to push Deepseek-OCR one step further. It is capable of one-shot long-horizon parsing.

## Configuration

This service requires a `.env` file to store your Hugging Face API token, which allows the container to download the model at runtime. A placeholder `.env` has been created for you.

Before deploying, make sure to configure your token in the `.env` file:
```bash
nano .env
```
*Set `HF_TOKEN` to your personal Hugging Face token.*

## Deployment

[docker-compose.yml](docker-compose.yml)

```yaml
services:
  unlimited-ocr:
    image: vllm/vllm-openai:unlimited-ocr
    container_name: unlimited-ocr
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN}
    volumes:
      - ./data:/root/.cache/huggingface
    command: --model baidu/Unlimited-OCR --served-model-name Unlimited-OCR --trust-remote-code --max-model-len 32768
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
```

To deploy this service, run:
```bash
docker compose up -d
```
