import json

# a Python object (dict):
# w = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# convert into JSON:
# z = json.dumps(w)

# the result is a JSON string:
# print(z)




# some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])


# acepta cualquier tipo de dato

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))




# ejemplo de uso

x = '''{
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}'''

# convert into JSON:
y = json.load(x)
# the result is a JSON string:
print(y)
# ppdemos darle formato al resultado

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4))
