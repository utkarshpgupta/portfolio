import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."

# Change working directory
os.chdir(DIRECTORY)

# Set up handler
handler = http.server.SimpleHTTPRequestHandler

# Launch browser automatically
url = f"http://localhost:{PORT}"
print(f"Serving at {url}")
webbrowser.open(url)

# Start server
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()
