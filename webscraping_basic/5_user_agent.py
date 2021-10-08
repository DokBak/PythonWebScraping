# 사이트에 접속시에 헤더정보로 스마트폰으로 접속인지, 컴퓨터로 접속인지의 정보가 전달되는데, 웹 크롤러의 경우에는 인증 정보가 아무것도 없기 때문에 403에러가 나온다.
# 
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"}
res = requests.get(url,headers=headers)
res.raise_for_status

with open("nadocoing.html","w",encoding="utf8" ) as f:
    f.write(res.text)