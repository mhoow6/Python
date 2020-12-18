import json

# JSON의 Key-Value 구조는 파이썬의 Dictionary로 변환되며 List는 List로 변환
data = '{"title": "Book1", "ISBN": "12345", "author": [{"name": "autho1", "age": 30}, {"name": "autho2", "age": 25}]}'

# JSON 형태의 문자열을 읽기 위해 loads()를 사용
json_data = json.loads(data)

# 키 이름을 문자열로 입력하면 값을 가져올 수 있습니다.
print(json_data['title'])
print(json_data['ISBN'])

for author in json_data['author']:
    print(author['name'])
    print(author['age'])