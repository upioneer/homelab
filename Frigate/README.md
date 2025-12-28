# Sample docker compose file
```yml
services:
  frigate:
    container_name: frigate
    restart: unless-stopped
    image: ghcr.io/blakeblackshear/frigate:0.16.3
    shm_size: "256mb" # shared memory for 10 cameras
#    devices:
#      - /dev/dri/renderD128:/dev/dri/renderD128 # ryzen igpu passthrough
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - ./config:/config  # SQLite DB lives here
      # ram disk for cache
      - type: tmpfs
        target: /tmp/cache
        tmpfs:
          size: 1000000000 # 1gb
      # ram disk for 247 recordings and events
      - type: tmpfs
        target: /media/frigate
        tmpfs:
          size: 8000000000 # 8gb buffer for history
    ports:
      - "1984:1984" # webrtc ui
#      - "5000:5000" # god mode port, disable once configured
      - "8554:8554" # go2rtc rstp
      - "8555:8555/tcp" #webrtc
      - "8555:8555/udp" #webrtc
      - "8971:8971" # main ui
    environment:
      - FRIGATE_RTSP_PASSWORD=${FRIGATE_RTSP_PASSWORD}
      - LIBVA_DRIVER_NAME=${LIBVA_DRIVER_NAME} # mandatory for ryzen 7945hx
```

# Sample /config/config.yml when used with a dual lens Reolink RLC-81MA
```yml
mqtt:
  enabled: false

go2rtc:
  streams:
    Cam1Wide:
      - ffmpeg:rtsp://dashboard:{FRIGATE_RTSP_PASSWORD}@192.168.x.x:554/h264Preview_01_sub#video=copy#audio=opus
    Cam1Tele:
      - ffmpeg:rtsp://dashboard:{FRIGATE_RTSP_PASSWORD}@192.168.x.x:554/h264Preview_02_sub#video=copy#audio=opus
  webrtc:
    candidates:
      - yourdomain.com:8555 # use if running thru reverse proxy
      - YourServerIP:8555
      - stun:8555

# Global Enriched Features
detect:
  enabled: true

snapshots:
  enabled: true
  timestamp: false
  bounding_box: true
  retain:
    default: 30

semantic_search:
  enabled: true
  model: jinav1 # recommended for CPU-only
  model_size: small

classification:
  bird:
    enabled: true

cameras:
  Cam1Wide:
    ffmpeg:
      inputs:
        - path: rtsp://127.0.0.1:8554/Cam1Wide
          roles: [record, detect]
    onvif:
      host: 192.168.x.x
      port: 8000
      user: dashboard
      password: '{FRIGATE_RTSP_PASSWORD}'

  Cam1Tele:
    ffmpeg:
      inputs:
        - path: rtsp://127.0.0.1:8554/Cam1Tele
          roles: [record, detect]

version: 0.16-0
```
