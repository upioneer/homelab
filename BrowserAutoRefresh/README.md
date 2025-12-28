# Browser Auto Refresh
- This shortcut will wrap a site in iframe and schedule an auto refresh per the meta tag cadence
- Update the "meta" if you need a quicker/longer delay between refreshes
- Update the "iframe src" tag with your site

```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="3600">
    <title>github.com/upioneer</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; overflow: hidden; }
        iframe { width: 100vw; height: 100vh; border: none; }
    </style>
</head>
<body>
    <iframe src="https://new-orleans.events/this-weekend/#schedule"></iframe>
</body>
</html>
```

# Tags and customization
Launch Chromium in kiosk mode. Effectively removes window borders and mouse cursor.
```
chromium-browser --kiosk /path/to/your/dashboard.html
```

Remove info bars
```
--incognito --noerrdialogs --disable-infobars
```
