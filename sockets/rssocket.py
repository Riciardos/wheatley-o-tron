import socket
import ssl


class RSSocket:

    buf_size = 1024

    def __init__(self, verb, host, path, headers, port=443, data_to_send=""):
        self._verb = verb
        self._host = host
        self._path = path
        self._headers = headers
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sslsocket = ssl.wrap_socket(self._socket)
        self._received_data = ""
        self._data_to_send = data_to_send
        self._connected = False

    def __enter__(self):
        self._sslsocket.connect((self._host, self._port))
        self._connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sslsocket.close()

    def connect(self):
        if not self._connected:
            self._sslsocket.connect((self._host, self._port))
            self._connected = True
        else:
            print("Already connected to {} on port {}".format(self._host, self._port))

    def format_headers(self):
        data = ""
        for header in self._headers:
            data += header + "\r\n"

        return data

    def do_request(self):
        self.connect()
        headers = self.format_headers()
        socket_data = "{} {} HTTP/1.1\r\nHost: {}\r\n{}\r\n".format(self._verb, self._path, self._host, headers)
        print(socket_data)
        self._sslsocket.send(bytes(socket_data, "utf-8"))

        received = str(self._sslsocket.recv(RSSocket.buf_size), "utf-8")
        print(received)
        while received:
            self._received_data += received
            received = str(self._sslsocket.recv(RSSocket.buf_size), "utf-8")
            print(received)
        self._sslsocket.close()
        return self._received_data







