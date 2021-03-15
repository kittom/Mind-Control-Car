import socket
import json


class pyWave:

    configStr = "{ 'enableRawOutput': 'enableRawOutput', 'format': 'Json'}"
    configByte = configStr.encode()
    val = 0

    def __init__(self, _host, _port):
        self.host = _host
        self.port = _port

    def connect(self):
        # This is a standard connection for an Internet socket
        # AF.INET is how you declare an internet socket

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the Thinkgear Connector
        client.connect((self.host, self.port))
        # calling this client to implement elsewhere

        client.send(self.configByte)

        return client

    def readData(self, _client):

        # This loop just waits for messages via the socket
        # while True:
        # The connection could break for lots of reasons to wrapping this in a try / catch
        try:
            # When a message is received write it to the data var
            #  uses a buffer to transfer packets, buffer size is 2^10
            data = _client.recv(1024)

            data_json = json.loads(data)
            eSenseData = data_json["eSense"]
            attention = eSenseData["attention"]
            self.val = attention
            return self.val

        # loop for
        except Exception as e:
            # print(str(e))
            if str(e) == "'eSense'":
                return self.val
            else:
                # print(e)
                return self.val



# testing code

if __name__ == '__main__':

    pywave = pyWave("localhost", 13854)
    client = pywave.connect()

    print("Waiting for data")
    while True:
        val = pywave.readData(client)
        print(val)


