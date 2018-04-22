from sockets import requests

if __name__=="__main__":

    url = "https://lichess.org/api/stream/event"
    headers = ["Authorization: Bearer F1sxoXphrD7bHIr0"]

    request = requests.GetRequest(url, headers)

    received = request.do_request()
    print(received)
