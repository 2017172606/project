# 작성자 : 이다빈
# Google PlayStore Application Review Crawling code

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_option)
driver.maximize_window()
# 접속
driver.get("https://play.google.com/store/games?device=windows")
driver.implicitly_wait(10)

# 어플 이름 검색
driver.find_element(By.XPATH,'/html/body/c-wiz[1]/header/nav/div/div[1]/button').click()
search_input = driver.find_element(By.XPATH,'/html/body/c-wiz[1]/header/nav/c-wiz/div/div/label/input')
search_input.send_keys("테이블링") # 크롤링하고자 하는 어플리케이션 이름
search_input.send_keys(Keys.ENTER)

time.sleep(2)
# 검색결과 a링크 클릭
driver.find_element(By.XPATH,'/html/body/c-wiz[3]/div/div/c-wiz/c-wiz[1]/c-wiz/section/div/div').click()
time.sleep(1)

# 리뷰 모두보기 클릭
for i in range(4):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

time.sleep(1)
driver.find_element(By.XPATH,'/html/body/c-wiz[4]/div/div/div[2]/div[2]/div/div[1]/div[1]/c-wiz[4]/section/div/div[2]/div[5]/div/div/button').click()

time.sleep(2)

# 제한된 리뷰만 보여주고 아래로 스크롤을 내리면 추가로 리뷰가 더 나타나는 방식.
# Web Element를 선택하고 send_key(keys.PAGE_DOWN)을 실행해도 창이 내려가지지 않음,
# 이러한 문제를 수동으로 해결. (웹페이지상 최하단까지 직접 내린다음에, y를 입력함으로)
while True:
    print("리뷰의 개수", len(driver.find_elements(By.CLASS_NAME,"h3YV2d")))
    a = input("구글 플레이스토어 리뷰 팝업이 스크롤링이 수동으로만 가능. 충분히 수집할 객체의 개수 만큼 내린 다음 y 입력")
    if a == 'y':
        break

comments = driver.find_elements(By.CLASS_NAME,"h3YV2d")
rating = driver.find_elements(By.CLASS_NAME,'iXRFPc')

comment = []
rate = []

for i in range(len(comments)):
    rate.append(rating[i].get_attribute("aria-label").split(" ")[3][0])
    if comments[i].text != "":
        comment.append(comments[i].text)
    else:
        comment.append("리뷰 없음")

# Dictionary를 간단하게 pandas DataFrame으로 만든 후에, 이를 csv로 변환

df_prev = {"평점":rate,
           "리뷰":comment}

df = pd.DataFrame(df_prev)

df.to_csv('테이블링어플 리뷰.csv',index=False)