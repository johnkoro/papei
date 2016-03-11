import json, urllib, re
url = 'http://api.openweathermap.org/data/2.5/weather?lat='
a = list(url)
X = raw_input("enter lat")
a.append(X)
a.append('&lon=')
Y = raw_input("enter lon")
a.append(Y)
a.append('&appid=c1e747662188b9652e8eb96a5c93475a')
str1 = ''.join(a)
json_obj = urllib.urlopen(str1)
data = json.load(json_obj)
weather= data[u'weather']
temp= data[u'main']
float_temp =temp[u'temp']
c_temp= float_temp - 273.15
if (c_temp < 5):
    print "brrrr..."
elif (c_temp >20):
    print "nice"
str2= ",".join(map(str, weather))
if u'Rain' in str2:
    print "I'm singing in the rain!"
    
