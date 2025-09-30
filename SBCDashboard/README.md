# SBC Dashboard
## SBC = Single Board Computers

---
Due to memory leaks, cache size and other factors, the experience with running sites 24/7 (ex: dashboards, twitch streams, youtube videos) can sometimes degrade with time to the point it stops rendering entirely. This requires a manual refresh to bring it back online until it crashes again.

Here are a few tips to improve your SBC dashboards:

---
# Create a script
```bash
#!/bin/bash
chromium-browser \
  --disable-features=Translate \
  --disable-sync \
  --no-errdialogs \
  --no-first-run \
  --kiosk "https://yourURL.com"
```
Flags to consider:

`--disable-gpu` Turns off hardware acceleration. The display might be less smooth, but more stable

`--disk-cache-size=10000000` Sets the disk cache size in bytes (10MB). Limiting the cache can prevent it from growing indefinitely

`--incognito` Incognito mode. This prevents writing to the cache and disables extensions, providing a cleaner session that can sometimes be more stable.

---
# Create a cron job to kill and restart the browser
Open cron editor
```bash
crontab -e
```

Example below: 3am, kill all Chromium processes and start a new one in kiosk mode on display 0
```bash
0 3 * * * pkill chromium-browser && export DISPLAY=:0 && /usr/bin/chromium-browser --kiosk "https://yourURL.com" >/dev/null 2>&1
```
