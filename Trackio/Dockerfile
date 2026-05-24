FROM python:3.10-slim

# Install trackio and its dependencies
RUN pip install --no-cache-dir trackio

# Expose the Gradio default port
EXPOSE 7860

# Set directory environment variable for caching and logs persistence
ENV TRACKIO_DIR=/data

# Run the Trackio visualization dashboard
CMD ["trackio", "show", "--host", "0.0.0.0", "--port", "7860"]
