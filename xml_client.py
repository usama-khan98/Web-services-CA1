from xmlrpc.server import SimpleXMLRPCServer

def get_temp(temp):
    if (temp >= 0 and temp <=10):
        return 'Cold'
    elif (temp >=11 and temp <=20):
        return 'Warm'

server = SimpleXMLRPCServer(("localhost", 8001))
print("Listening on port 8001...")
server.register_function(get_temp, "get_temp")
server.serve_forever()
