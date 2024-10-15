# import json
# file = open("posts.json","r")

# x = file.read()
# finaldata = json.loads(x)

# print(finaldata)

# import json

# # Opening JSON file
# with open('posts.json', 'r') as f:
#     data = json.load(f)

# # Using the data as a Python dictionary
# for entry in data:
#     print(entry)


import json

# Opening JSON file
f = open('posts.json')

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data:
    print(i)

# Closing file
f.close()
