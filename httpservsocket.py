#!/usr/bin/python3

### Start a basic http server, listening on port 666, serving a basic
### index.html file with check_mk formatted output

import http.server
import socketserver
import os

PORT = 666

# change dir to serve the relative dir index.html file
os.chdir('/root/realitycheck/')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
