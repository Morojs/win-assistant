from urllib.parse import urlencode
from urllib.request import Request, urlopen


def get_answer(text):
    f = open("response.json", "w")
    # url = "http://api.wolframalpha.com/v2/query?appid="  # Set destination URL here
    url = "https://api.wolframalpha.com/v1/result?appid="  # Set destination URL here
    post_fields = {
        "i": text,
        "output": "JSON",
    }  # Set POST fields here
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    f.write(json)
    f.close()
    # open and read the file after the appending:
    f = open("response.json", "r")
    return f.read()
