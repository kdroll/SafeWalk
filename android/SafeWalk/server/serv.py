import time
import BaseHTTPServer
import json


HOST_NAME = '192.168.1.68' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080 # Maybe set this to 9000.

#need to add a setting temp for right now in app for ip of server. Right now it is hard coded


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()


    # this will be a request from the app for information, server will send json to app.     
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")

    #respond to POST Request, which will come from Safewalk App
    def do_POST(self):
        print("Got a post!")
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        #postBody is a dictionary with key-value pairs of json values
        marked = json.loads(post_body)
        for item in marked.values():
            print(item)
            print("\n")
        #for right now, I just print the values



#start the class, press CTRL C to stop the server
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    print("Hit CTRL C to stop server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)