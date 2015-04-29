import BaseHTTPServer
import subprocess
import re


class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	package_name_pattern=re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)*$')

	def do_GET(self):
		if re.match(self.package_name_pattern, self.path[1:]):
			self.index(self.path[1:])
		else:
			self.send_error(404)

	def index(self, package_name):
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Content-Type', 'text/html')
		self.end_headers()
		data = subprocess.check_output(['adb', 'shell', 'dumpsys', 'gfxinfo', package_name])
		self.wfile.write(data)


def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
	run(BaseHTTPServer.HTTPServer, MyRequestHandler)
