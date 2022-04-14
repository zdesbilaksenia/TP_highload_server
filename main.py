import server.internal.handler as handler
import server.internal.server as server

if __name__ == '__main__':
    server = server.Server(handler=handler.ServerHandler())
    server.run()
