## 외부모듈
# - 파이썬 이외의 다른 기관이나 SW회사 등에서 배포한 모듈로 특정 기능을 제공하는 모듈
    # -> 공개 소스 라이센스 계약에 따라 개발한 소프트웨어를 다른 사용자가 사용 가능
    # -> 다양한 사용자층과 커뮤니티가 활성화 되어 있음
# - 4차 산업혁명 관련 IT 분야에서 파이썬의 중요성이 높아지고 있음
# - 해당 분야의 프로그래밍에 도움되는 외부모듈을 다양하게 제공
    # 데이터 분석, 통계 : Numpy, Pandas, matlotilb ...
    # 인공지능 : Tensorflow, PyTorch, Keras ...
    # 웹 크롤링 : BeautifulSoup, Selenium ...

## 외부모듈설치
# - 패키지 관리자 사용하기(PIP)
    # -> 파이썬 3.4 이후 버전은 기본적으로 pip를 포함하고 있으며, 손쉽게 외부 모듈을 설치할 수 있음

# 콘솔(터미널)창에서 pip install 패키지명 한 줄로 외부 모듈 설치 가능
    # 예: pip install padnas

# 쥬피터 노트북 환경에서 명령어 앞 !를 붙여 설치 가능 -> 느낌표를 붙이면 콘솔창에서 입력하는 것과 같은 역할을 함
# !pip install pandas
import pandas as pd
print(pd.__version__) # 2.3.3



## 웹 크롤링
# - 컴퓨터 소프트웨어 기술로 웹 사이트들에서 원하는 정보를 추출하는 것

# BeautifulSoup 설치
# pip install beautifulsoup4

from bs4 import BeautifulSoup


## 네이버 웹소설 통합 랭킹 소설 이름 가져오기

# urllib 모듈로 웹 페이지 가져오기
    # - 파이썬에서 웹과 관련되 작업을 도와주는 모듈
    # - 데이터를 가져오는 역할을 하는 urllib 중 request 모듈을 활용해 웹소설 메인 페이지 정보를 가져옴
# import urllib.request as req

# html_page = req.urlopen("https://novel.naver.com/webnovel/weekday")
# print(html_page.read())

# BeautifulSoup 모듈로 웹 페이지 분석
    # - 텍스트화된 웹 페이지는 BeautifulSoup 모둘을 활용하면 HTML 태그 단위로 분석 가능
# import bs4

# result = bs4.BeautifulSoup(html_page, "html.parser")
# print(result)

# rank_block = result.select("ul.ranking_list li.item p.title_group span.title")
# print(rank_block)

# print(len(rank_block))
# for index, item_title in enumerate(rank_block):
#     rank_title = str(item_title).split(">")[1].split("<")[0]
#     print(index+1, "위\t", rank_title)


import urllib.request as req
from bs4 import BeautifulSoup

# 웹 페이지 가져오기
url = "https://novel.naver.com/webnovel/weekday"
html_page = req.urlopen(url)

# BeautifulSoup으로 분석
soup = BeautifulSoup(html_page, "html.parser")

# 소설 제목 선택
rank_block = soup.select("ul.ranking_list li.item p.title_group span.title")

# 출력
for index, item in enumerate(rank_block, start=1):
    title = item.text.strip()
    print(f"{index}위\t{title}")
