import tornado.ioloop
import tornado.web
import socket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888,socket.gethostbyname(socket.gethostname()))
    tornado.ioloop.IOLoop.current().start()
