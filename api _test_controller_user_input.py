import requests
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse
    from urllib.parse import urlencode

print('LA City Controller Checkbook API scrapper \n')

url = "https://controllerdata.lacity.org/resource/pggv-e4fn.json"
params = {'id_number':None,'department_name':None,'vendor_name':None}

id_num = str(input("ENTER ID NUMBER: \n"))
print(id_num)
params["id_number"] = id_num

def cleanNullTerms(params):                                                                             #function clears any key with the value of None
   return {
      k:v
      for k, v in params.items()
      if v is not None
   }

params2 = cleanNullTerms(params)

url_parts = list(urllib.parse.urlparse(url))                                                            #urlparse is a function that returns an obejct that acts like a tuple wtih 6 elements
query = dict(urllib.parse.parse_qsl(url_parts[4]))                                                      #query is the 5th element in tuple. This element becomes space for dictionary entries
query.update(params2)

url_parts[4] = urlencode(query)                                                                         #encodes dictionary entries to be a part of url

print('URL: ' + urllib.parse.urlunparse(url_parts) + '\n')

r = urllib.parse.urlunparse(url_parts)

s = requests.get(r)
print(s.text)
