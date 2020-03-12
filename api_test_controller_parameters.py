import requests
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse
    from urllib.parse import urlencode

url = "https://controllerdata.lacity.org/resource/pggv-e4fn.json"
params = {'id_number':'6378807','department_name':'TRANSPORTATION','vendor_name':'VERIZON WIRELESS'}

url_parts = list(urllib.parse.urlparse(url))                                                            #urlparse is a function that returns an obejct that acts like a tuple wtih 6 elements
query = dict(urllib.parse.parse_qsl(url_parts[4]))                                                      #query is the 5th element in tuple. This element becomes space for dictionary entries
query.update(params)

url_parts[4] = urlencode(query)                                                                         #encodes dictionary entries to be a part of url

print(urllib.parse.urlunparse(url_parts))

r = urllib.parse.urlunparse(url_parts)

s = requests.get(r)
print(s.text)
