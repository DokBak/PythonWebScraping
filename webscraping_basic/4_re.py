# 정규식 (regular expression)
# 주민등록번호, 이메일 주소와 같이 정해진 규칙이 있는 경우에 효율적으로 검색하기 편한 방식

import re

# 아래와 같이 4글자의 데이터를 찾을 것
# abcd, book, desk

# 다음과 같이 3번째 글자만 모를 경우의 검색방법은?
# ca?e
# care, cafe, case, cave 등 알고 있는 문자들로 검색을 실시하던가
# caae, cabe, cace, cade, ... 와같이 a부터 순차적으로 전부 수작업으로 검색하는 코드를 작성하는 방법이 있지만 
# 모르는 부분이 다수 있거나 할 경우에는 패턴의 종류 또한 많아진다. 이럴때 사용하는 것이 정규식표현

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미  > care, cafe, case 등등 caffe는 총 5글자의 문자열이기에 검색되지 않는다.
# ^ (^de) : 문자열의 시작 > desk, destination 등등 fade는 de로 시작되지 않기에 검색되지 않는다.
# $ (se$) : 문자열의 끝 > case. base 등등 face는 문자열의 끝이 se로 끝나지 않기에 검색되지 않는다.

def print_match(m):
    # m = p.match("case")

    # print(m.group()) # 매치되지 않으면 에러가 발생 
    if m:
        print("m.group() : ", m.group() ) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 일치하는 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("case")
print("p.match(\"case\")")
print_match(m)

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print("p.match(\"caseless\")")
print_match(m)

m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print("p.search(\"caseless\")")
print_match(m)

lst = p.findall("careless cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print("p.findall(\"caseless cafe\")")
print(lst) 


# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. lst = p.findall("비교할 문자열")

# 원하는 형태 : 정규식
# . (ca.e): 하나의 문자를 의미  > care, cafe, case 등등 caffe는 총 5글자의 문자열이기에 검색되지 않는다.
# ^ (^de) : 문자열의 시작 > desk, destination 등등 fade는 de로 시작되지 않기에 검색되지 않는다.
# $ (se$) : 문자열의 끝 > case. base 등등 face는 문자열의 끝이 se로 끝나지 않기에 검색되지 않는다.

# 추가적인 정규식 표현에 대한 공부 방법
# 1. w3school 에서 Python RegEx에서 공부를 하는 방법
# 2. python re로 검색해서 나오는 docs.python.org의 파이썬 공식 문서를 참조하여 공부하는 방법