
import sys

from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the server address and port
server_address = ("", 8000)  # "" means listen on all available IPs, 8000 is the port

# Create the HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(sys.version)
print("Serving on port 8000...")
httpd.serve_forever()  # Start the server
