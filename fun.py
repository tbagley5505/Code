
def url_ver(url):
    domains = [".com", ".net", ".edu", ".gov"]
    if isinstance(url, str):
        if url.endswith((tuple(domains))):
            print("right")
        else:
            print("Please enter a vaild URL")
            return None
    else:
        print("Please enter a vaild UL")
        return None

url = 23
url_ver(url)