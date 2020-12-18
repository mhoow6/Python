import json
from io import StringIO

book = {'title': 'Book1', 'ISBN': '12345', 'author': [{'name': 'autho1', 'age': 30}, {'name': 'autho2', 'age': 25}]}
io = StringIO()
json.dump(book, io)
print(io.getvalue())
print('')

io = StringIO()
json.dump(book, io, indent=4)
print(io.getvalue())