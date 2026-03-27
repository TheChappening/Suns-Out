import http.server, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass

http.server.HTTPServer(('', 3456), Handler).serve_forever()
