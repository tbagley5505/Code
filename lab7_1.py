# NOTE: Throughout, if there is an error that you need to deal with
# like the input string was not valid URL, then your function should
# return None.

# Add a line to import the requests library 
import requests
# res = [i for i in test_list if subs in i]
#: Build a URL verification function. You may use any name that 
# you like for the function as I will not be testing it with 
# unittests. This function should take a string as a parameter.
# It must test:
# 1. The string must end with one of the following four top level 
# domains: .com, .net, .edu, .gov. This means checking the last three
# characters. If this test fails, the function should return None  
# If the url is okay, then this function should return a string of the URL.

def url_ver(url):
    domains = [".com", ".net", ".edu", ".gov"]
    if isinstance(url, str):
        if url.endswith((tuple(domains))):
            return url
        else:
            print("Please enter a vaild URL")
            return None
    else:
        print("Please enter a vaild URL")
        return None

#  Create a function called basic_request() that takes a url as a 
# string as a parameter.
# First, use the URL verification function above to verify, fix, or fail
# the URL. If that function returns None, this function should return None.
# Second, once the URL is checked and fixed as needed the function will
# use the requests library to make a GET request to that url and store 
# the status code to a variable called sc. Return the status code.
#  there are other libraries that could be used, but you must 
# use the requests library for this to be correct.

def basic_request(url):
    if url_ver(url):
        return requests.get(url).status_code 
    return None
     
# TODO: Create a function called request_user_agent() that will take two 
# parameters.
# The first parameter will be a URL. Again, check it with the first
# function you created.
# The second parameter will be a string that is the user agent. User 
# agent is a code that gets sent with a request that identifies the 
# program making the request. If this parameter is not a string, return
# None.
# Your function must then make a request to the URL parameter using 
# the user agent. You'll need to read the documentation for requests
# if you want to do this part.
# You should return the text of the response. It is a secret code 
# that is on a live server and is needed to pass the unittest.
# {'user-agent': 'my-app/0.0.1'}
def request_user_agent(url, sc):
    if url_ver(url):
        if requests.get(url):
            headers = {'user-agent': 'my-app/0.0.1'}
            if isinstance(headers, str):
                headers = requests.get(url, headers=headers)
                return headers
            return None
        else:
            return None
    else:
        return None

# TODO: Create a function called request_post() that takes a url and 
# a dictionary as parameters. 
# Again use your verification function to check the URL
# If the URL is not good, return None. 
# You'll also need to check the data coming in as the second
# parameter. We won't do anything more than verify that it is not 
# empty. So if the data is empty or None or not a dictionary, then
# your function should return None.
# If the parameters check out, then your function should send a post
# request to the URL.
# When you make this call, correctly, the server will send back a 
# code as the text property of the response (as in the 
# request_user_agent() function above).
# Your function will return the code.
def request_post(url, dic):
    if url_ver(url):
        if r = requests.post(url, data = dic)
            if dic is None
                return None
            else: 
                r = requests.post(url, data = {'key':'value'})
        return None
    else:
        return None
       