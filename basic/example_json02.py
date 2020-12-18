import json
from io import StringIO

# 메모리의 데이터를 파일처럼 읽을 수 있는 StringIO를 활용해서 파일에서 읽음
io = StringIO('{"title": "Book1", "ISBN": "12345", "author": [{"name": "autho1", "age": 30}, {"name": "autho2", "age": 25}]}')

# load() 메소드를 사용하면 파일의 내용을 읽어 오는 것도 가능
json_data = json.load(io)

print(json_data['title'])
print(json_data['ISBN'])

for author in json_data['author']:
    print(author['name'])
    print(author['age'])