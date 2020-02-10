import requests
r = requests.get('https://controllerdata.lacity.org/resource/pggv-e4fn.json?id_number=6378807&department_name=TRANSPORTATION&vendor_name=VERIZON WIRELESS')
print(r.text)
