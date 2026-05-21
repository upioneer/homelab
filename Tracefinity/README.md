# Tracefinity

[Tracefinity](https://tracefinity.net/) is an open-source, self-hosted web tool that uses AI models to generate custom Gridfinity bins from photos of your physical tools.

## Deployment

1.  Deploy using Docker Compose:
    ```bash
    docker compose up -d
    ```

## Features

- **AI-Powered Tracing:** Automatically extract the precise outline of tools from photos using state-of-the-art vision models.
- **Flexible AI backends:** Run tracing locally using lightweight ONNX models (e.g., IS-Net) or plug in your Google Gemini API key for high-fidelity cloud tracing.
- **Automatic Scale Calibration:** Simply place your tools on a standard sheet of paper (A4 or US Letter) to let the system calibrate dimensions automatically.
- **Gridfinity Integration:** Arrange the generated tool outlines in customized organizer trays and export the design as 3D-printable STL or 3MF files.

For more information, visit the [official website](https://tracefinity.net/) or the [GitHub repository](https://github.com/tracefinity/tracefinity).
