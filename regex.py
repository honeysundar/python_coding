import re

txt = "The rain in india"

#Check if "Portugal" is in the string:

x = re.findall("india", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  

