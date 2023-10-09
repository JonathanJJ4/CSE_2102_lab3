import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'''This is Jonathan Jawahar's website!\n         _     _
        /\`-"-`/\\
        )` _ _ `(
       {=   Y   =}
        \   ^   /
       /`;'-u-';`\\
      | /       \ |
     /\ ;__\ / _/ /
     \___, )~(,,),)
        (_(''')



httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
