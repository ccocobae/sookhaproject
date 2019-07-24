import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

db = TinyDB('/Users/soo/Pycharmprojects/sookhaproject/forstudy/July26th/databases/database.db', default_table='users')

# 메모리 DB 생성
# db = TinyDB(storage=MemoryStorage, default_table='users')

# 테이블 선택, 데이터 타입 : json
users = db.table('users')
todos = db.table('todos')

# 테이블 데이터 전체 삽입 1
with open('/Users/soo/Pycharmprojects/sookhaproject/forstudy/July26th/data/users.json', 'r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

with open('/Users/soo/Pycharmprojects/sookhaproject/forstudy/July26th/data/todos.json', 'r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)

# 전체 데이터 출력
print(users.all())
print(todos.all())

# 테이블 목록
print(db.tables())

# 전체 데이터 삭제
# users.purge()  # db.purge_table('users')
# todos.purge()

# db.purge_tables()

db.close()