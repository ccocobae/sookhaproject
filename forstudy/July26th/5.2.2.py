import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query, where

db = TinyDB('/Users/soo/Pycharmprojects/sookhaproject/forstudy/July26th/databases/database.db', default_table='users')

# 메모리 DB 생성
# db = TinyDB(storage=MemoryStorage, default_table='users')

# 테이블 선택, 데이터 타입 : json
users = db.table('users')
todos = db.table('todos')

# for item in users:
#     print(item['username'], ':', item['phone'])
#
# for item in todos:
#     print(item['title'], ':', item['completed'])

for item in users:
    print('[', item['username'], ']')
    for todo in todos:
        if todo['userId'] == item['id']:
            print(todo['title'])

# >쿼리 객체< 사용 조회
# SQL = Query()
Users = Query()
Todos = Query()

# Row 수정
users.update({'username': 'Nam'}, Users.id == 3)

user_3 = users.search(Users.id == 3)
print(user_3)

# Users 여러가지 조회 방법
print(users.search(Users['id'] == 7))
print(users.search(where('id') == 7))
print(users.search(Query()['id'] == 7))
print(users.search(where('address')['zipcode'] == '90566-7771'))  # 딕셔너리 속 딕셔너리 형태
print(users.search(where('address').zipcode == '90566-7771'))

# 고급 쿼리
print(users.search(Users.email.exists()))  # email 을 가진 row 를 다 불러옴

# NOT
print('not :', users.search(~(Users.username == 'Antonette')))  # ~ 사용

# OR
print('or :', users.search((Users.username == 'Antonette') | (Users.username == 'Kamren')))

# AND
print('and :', users.search((Users.username == 'Antonette') & (Users.id == 2)))

# 기타 함수
print('len :', len(users))
print('len :', len(todos))
print('contains', users.contains(Users.username == 'Kamren'))
print('count', users.count(Users.username == 'Kamren'))