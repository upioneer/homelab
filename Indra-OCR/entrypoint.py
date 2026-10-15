#!/usr/bin/env python3
import sys
import indra_ocr.viewer as v

# Monkeypatch ThreadingHTTPServer in indra_ocr.viewer so it binds to 0.0.0.0
# instead of 127.0.0.1, making the web UI accessible outside the container.
orig_server = v.ThreadingHTTPServer
v.ThreadingHTTPServer = lambda addr, handler: orig_server(("0.0.0.0", addr[1]), handler)

if __name__ == "__main__":
    v.main()
