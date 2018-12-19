import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import time
import random
import requestHandler

FILE = 'web/index.html'
PORT = 2009


class RubotHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_HEAD(self):
		print "send header"
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()


	def do_GET(self):
		f = self.send_head()
		if f:
			self.copyfile(f, self.wfile)
			f.close()


	def do_POST(self):
		length = int(self.headers.getheader('content-length'))
		data = self.rfile.read(length)
		print data
		requestHandler.processRequest(data)



	def open_browser():
		thread.start()

def start_server():
	server_address = ("", PORT)
	server = BaseHTTPServer.HTTPServer(server_address, RubotHandler)
	server.serve_forever()



if __name__ == "__main__":
    start_server()
