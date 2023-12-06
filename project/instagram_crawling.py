# 작성자 : 이다빈
# 인스타그램 게시글 크롤링 코드
# 웨이팅 해시태그 관련 게시글 코드를 크롤링 하는 코드입니다.
# 인스타그램 PC버전이 얼마전부터 최근 업로드 한 글을 조회할 수 없게 막으면서 크롤링이 막혔습니다. 그러나,
# 휴대폰으로는 인기글 뿐만 아니라 최근 업데이트 글까지 불러올 수 있기에, 휴대폰을 통해서 게시글의 URL을
# 가져오는 방식으로 생성하였습니다.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

a = ['https://www.instagram.com/p/Cq77AtIv5SO/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/reel/C0VyqnaSUHk/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/reel/CrOH856AVH-/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0YkxclP04O/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CFNzMSNBQLd/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CyQCPpiu35o/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/Ca_CusthjOt/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0OMWVbJwJI/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0gjPLoJLrb/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0d7l5zPDxf/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CWmvI2EFtJN/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CmIxk37SoWn/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0eI4xxp8kd/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0alY8kyXHQ/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/reel/C0bNNeQyN6s/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CmIsbmkOrDa/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CQNvHFOlFlZ/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0RWgZ2S69t/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0gVmUmSuQ8/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CqPiWtLSlaS/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0T03p_yqOZ/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0fsb6nSCUb/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0gZoC9LEdD/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CnzExdPrwaL/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0g4XTeyUl2/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0bS9i-LhfH/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0OIEluvoHu/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CwOz8hRvKvR/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/reel/Cw7QHzaSNNt/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CfBQsWnldit/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0IcTYNyaMF/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CrkbftWy9z1/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/Cn100izrOly/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0QXXkIyLht/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CnjuefKSETk/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0NeQTYS3-M/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0JDvLKpyp0/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/Cl22SVcLAT7/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0LLOBmymL3/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0JGuRFSFom/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0OeIXoyF5K/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CMJFMz_Fa6Z/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0Q8oxcxV9w/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0bGBQILyXO/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/CHyk2hvJRgf/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0CBdtOyubx/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0O1OgKSsbI/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0EkEhyrEUN/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/C0Gghj3RKtN/?igshid=MzRlODBiNWFlZA==',
     'https://www.instagram.com/p/ClnZrsArEOK/?igshid=MzRlODBiNWFlZA==']

print(len(a))

chrome_options = Options()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

frame = {}
post = []

for i, link in enumerate(a):
    print(i+1)
    driver.get(link)
    time.sleep(10)
    content = driver.find_element(By.CSS_SELECTOR,'h1._ap3a._aaco._aacu._aacx._aad7._aade')
    post.append(content.text)


frame["게시글"] = post
pd.DataFrame(frame).to_csv('인스타그램 웨이팅 해시태그 연관 게시글.csv',index=False)
