#how many recycling centers within 10 miles are at some zipcode
from urllib.request import urlopen
import re



ourUrl = "https://search.earth911.com/?what=CFLs%2C+desktop+computers%2C+cell+phones%2C+etc...&where="
ourUrl += "91701" #TODO: Switch to an actual variable
ourUrl += "&list_filter=all&max_distance=10&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="

pageRecycle = urlopen(ourUrl) #returns an HTTPResponse object
html_bytes = pageRecycle.read()
#html = html_bytes.decode("utf-8")

numResults = hmtl_bytes.count("result-item")
print(numResults)




#get number of occurrences of the substring
#in the string
#occurrences = data.count("python")
