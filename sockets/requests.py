from .rssocket import RSSocket


class UrlRequest(RSSocket):

    def __init__(self, verb, url, headers, data_to_send=""):

        if url[:4] == "http":
            if url[4] == "s":
                port = 443
            else:
                port = 80
        else:
            raise Exception

        url_array = url.split("/")
        host = url_array[2]
        path = "/"
        if len(url_array) > 3:
            path += "/".join(url_array[3:])

        super().__init__(verb, host, path, headers, port=port, data_to_send=data_to_send)

    def do_request(self):
        return super().do_request()


class GetRequest(UrlRequest):

    def __init__(self, url, headers):
        super().__init__("GET", url, headers)

    def do_request(self):
        return super().do_request()


class GetStreamRequest(UrlRequest):

    def __init__(self, url, headers):
        super().__init__("GET", url, headers)

    def do_request(self):
        return super().do_request()


class PostRequest(UrlRequest):

    def __init__(self, url, headers, data):
        super().__init__("POST", url, headers, data_to_send=data)

    def do_request(self):
        return super().do_request()
