import json

# book은 파이썬의 Dictionary 타입으로 dumps()를 호출하면 String으로 변환
book = {'title': 'Book1', 'ISBN': '12345', 'author': [{'name': 'autho1', 'age': 30}, {'name': 'autho2', 'age': 25}]}

print(json.dumps(book))
print('')

# indent를 지정하지 않으면 포맷팅이 되지 않은 문자열로 표시된다
print(json.dumps(book, indent=2))