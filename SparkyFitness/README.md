# SparkyFitness

[SparkyFitness](https://github.com/CodeWithCJ/SparkyFitness) is a self-hosted, privacy-first fitness and nutrition tracking platform. It is designed as an alternative to MyFitnessPal, with a focus on family use and AI-powered features.

## Deployment

1.  Copy `example.env` to `.env`:
    ```bash
    cp example.env .env
    ```
2.  Update the environment variables in `.env`, especially the security keys.
3.  Deploy using Docker Compose:
    ```bash
    docker compose up -d
    ```

## Features

- **Comprehensive Tracking:** Monitor food (nutrition), exercise, water intake, and body metrics.
- **AI-Powered:** Includes an AI chatbot for health and fitness insights.
- **Privacy-Focused:** Maintain full control over your data by self-hosting.
- **Family Support:** Designed for families to track health together.

For more information, visit the [official documentation](https://codewithcj.github.io/SparkyFitness/) or the [GitHub repository](https://github.com/CodeWithCJ/SparkyFitness).
