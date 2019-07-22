import simplejson as json
# import json

# Dict(json) 선언
data = {}

data['people'] = []
data['people'].append({
    'name': 'Nam',
    'website': 'google.com',
    'from': 'Daejeon',
    'grade': [99, 88, 77]
})
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
    'grade': [98, 86, 78]
})
data['people'].append({
    'name': 'Park',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [96, 86, 76]
})

# Dict(Json) -> Str : 파일로 작성 가능
e = json.dumps(data)
# print(type(e))  # str
# print(e)

# Str -> Dict(Json)
d = json.loads(e)
# print(type(d))  # dict
# print(d)

with open('/Users/soo/PycharmProjects/crawling/July22th/members.json', 'w') as outfile:
    outfile.write(e)  # json editor 사용하면 편하게 볼 수 있음

with open('/Users/soo/PycharmProjects/crawling/July22th/members.json', 'r') as infile:
    r = json.load(infile)
    print(type(r))
    for p in r['people']:
        print("Name: " + p['name'])
        print("website: " + p['website'])
        print("From: " + p['from'])
        grade = ''
        for g in p['grade']:
            grade += ' ' + str(g)
        print("Grade: " + grade.lstrip())
        print()
