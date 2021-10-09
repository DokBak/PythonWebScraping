import requests
from bs4 import BeautifulSoup # BeautifulSoup은 웹스크래핑을 하는데 사용되는 패키지

# 
url = "https://comic.naver.com/webtoon/weekday"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # url에 해당하는 requests정보를 BeautifulSoup객체로 만든다. 
                                       # lxml은 특정구문을 분석해 파싱하는 패키지

print(soup.title)

print(soup.title.get_text()) # 타이틀의 text값만 가져온다.

print(soup.a) # soup객체가 가지고 있는 모든 객체중에서 처음으로 등장하는 a태그(a element) 값을 표시

print(soup.a.attrs) # a태그(a element)의 속성을 표시(attrs)

print(soup.a["href"]) # a태그(a element)의 속성중에서 href속성 값을 표시

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a태그중에서 속성 class의 값이 "Nbtn_upload"인 첫 번째 element를 표시

print(soup.find(attrs={"class":"Nbtn_upload"})) # a태그라는 내용을 제외한 경우는 클래스속성이 동일한 다른 태그가 검색되기도 하기에 정확하게 검색을 위해서라면 태그를 지정하는 것이 좋다.
                                                # 속성 class의 값이 "Nbtn_upload"인 첫 번째 element를 표시

print(soup.find("li", attrs={"class":"rank01"})) 
rank1 = soup.find("li", attrs={"class":"rank01"}) # 검색한 태그의 하위 태그의 정보만을 가져올때는 검색 태그 정보를 변수로 담아
print(rank1.a)                                    # 원하는 태그를 반환한다.