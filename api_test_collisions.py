import requests
import json




################################################################################


print("Total number of yearly collisions data \n")
print("\n")
print("\n")

i = True

while i:
    choice = str(input("Choose a year between 2010 and 2019: \n"))
    if choice == "2010":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2010-01-01T00:00:00.000'+and+'2010-12-31T00:00:00.000'"
        break

    elif choice == "2011":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2011-01-01T00:00:00.000'+and+'2011-12-31T00:00:00.000'"
        break

    elif choice == "2012":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2012-01-01T00:00:00.000'+and+'2012-12-31T00:00:00.000'"
        break

    elif choice == "2013":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2013-01-01T00:00:00.000'+and+'2013-12-31T00:00:00.000'"
        break

    elif choice == "2014":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2014-01-01T00:00:00.000'+and+'2014-12-31T00:00:00.000'"
        break

    elif choice == "2015":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2015-01-01T00:00:00.000'+and+'2015-12-31T00:00:00.000'"
        break

    elif choice == "2016":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2016-01-01T00:00:00.000'+and+'2016-12-31T00:00:00.000'"
        break

    elif choice == "2017":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2017-01-01T00:00:00.000'+and+'2017-12-31T00:00:00.000'"
        break

    elif choice == "2018":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2018-01-01T00:00:00.000'+and+'2018-12-31T00:00:00.000'"
        break

    elif choice == "2019":
        url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2019-01-01T00:00:00.000'+and+'2019-12-31T00:00:00.000'"
        break

    else:
        print("Invalid date try again")
        break


s = requests.get(url)

json_object = json.loads(s.text)

json_pretty = json.dumps(json_object, indent=2)

print(json_pretty)







#url = "https://data.lacity.org/resource/d5tf-ez2w.json?$where=date_occ+between+'2015-01-10T00:00:00.000'+and+'2015-01-11T00:00:00.000'"

#r = requests.get(url)

#print(r.text)
