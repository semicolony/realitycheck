#!/usr/bin/python3

### Start a basic http server, listening on port 666, serving a basic
### index.html file with check_mk formatted output

import http.server
import socketserver

PORT = 666

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
