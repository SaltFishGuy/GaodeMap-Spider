from http.server import HTTPServer,CGIHTTPRequestHandler
import cgi

PORT = 8000

httpd = HTTPServer(("",PORT),CGIHTTPRequestHandler)

form = cgi.FieldStorage()

print("serving at port",PORT)

httpd.serve_forever()