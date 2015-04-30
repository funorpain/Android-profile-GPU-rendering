import BaseHTTPServer
import subprocess
import re


__version__ = "0.1"


class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	server_version = "apgr/" + __version__
	protocol_version = "HTTP/1.1"
	package_name_pattern=re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)*$')

	def do_GET(self):
		if re.match(self.package_name_pattern, self.path[1:]):
			self.index(self.path[1:])
		else:
			self.send_error(404)

	def index(self, package_name):
		data = subprocess.check_output(['adb', 'shell', 'dumpsys', 'gfxinfo', package_name])

		self.send_response(200)
		self.send_header('Connection', 'keep-alive')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Content-Type', 'text/html')
		self.send_header('Content-Length', len(data))
		self.end_headers()

		self.wfile.write(data)


def test(HandlerClass = MyRequestHandler,
		 ServerClass = BaseHTTPServer.HTTPServer):
    server_address = ('', 8002)
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == '__main__':
	test()
