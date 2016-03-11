import json, urllib, re
from collections import Counter
url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/'
a = list(url)
X = raw_input("Enter data as dd-mm-yyyy: ")
a.extend(X)
a.append(".json")
str1 = ''.join(a)
json_obj = urllib.urlopen(str1)
data = json.load(json_obj)
str2 = str(data)
v = str2.replace('-', '')
z = re.findall('\d+', v)
results = map(int, z)
for i in range(1,81):
    print "ο αριθμός", i, "εμφανίστηκε:", results.count(i), "φορές"





    




           
