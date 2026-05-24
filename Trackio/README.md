# Trackio

[Trackio](https://github.com/gradio-app/trackio) is a lightweight, local-first machine learning experiment tracking tool built by Hugging Face and the Gradio team. It serves as a simple, drop-in alternative to heavier tracking platforms like Weights & Biases (wandb).

This directory contains containerization configs to host the Trackio dashboard locally in your homelab.

## Getting Started

### Launching the Dashboard

To build and run the Trackio dashboard:

```bash
docker compose up -d --build
```

Once running, the interactive dashboard is accessible at:
👉 **[http://localhost:7860](http://localhost:7860)**

---

## Usage in Python Applications

Using Trackio in your machine learning pipelines is straightforward and highly compatible with standard experiment tracking workflows.

### 1. Installation

Install the library in your training environment:

```bash
pip install trackio
```

### 2. Basic Example

Initialize the `Tracker` and log your metrics:

```python
import time
import random
from trackio import Tracker

# Start a tracking run
tracker = Tracker(project_name="mnist-classifier", run_name="resnet-18-baseline")

# Simulate training loop
for epoch in range(1, 11):
    loss = 0.5 / epoch + random.uniform(-0.02, 0.02)
    accuracy = 0.7 + (0.25 * (epoch / 10)) + random.uniform(-0.01, 0.01)
    
    # Log metrics to Trackio
    tracker.log({
        "epoch": epoch,
        "loss": loss,
        "accuracy": accuracy
    })
    time.sleep(0.5)

# Mark the run as finished
tracker.finish()
```

### 3. Pointing to your Self-Hosted Server

To view metrics logged from your local scripts inside your self-hosted dashboard, ensure the logging runs write to the directory mounted in your Docker container or sync using Hugging Face Spaces.
