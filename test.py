from selenium import webdriver

# 페이지 스크롤링을 위한 모듈
from selenium.webdriver.common.keys import Keys

# 다운로드 받은 드라이버 주소
DRIVER_DIR = 'driver2/chromedriver'

driver = webdriver.Chrome(DRIVER_DIR)

# 목표 웹페이지를 가져옴
url = "https://www.us.kohler.com/us/browse/kitchen-kitchen-sinks/_/N-25b4"
driver.get(url)


# 상품명 가져오기
item_list = driver.find_elements_by_css_selector('.product-panel__summary.product-panel__summary-new')
item = []
for i in item_list:
    item.append(i.text)

len(item)

# 가격 가져오기
price_list = driver.find_elements_by_css_selector('.product-panel__price.product-panel__price-new.light-gray--sku--price.promo-price-discountprice-nk')
price = []
for p in price_list:
    price.append(p.text)

len(price)



# 데이터프레임으로 만들기
import pandas as pd

data_tuples = list(zip(item, price))

df = pd.DataFrame(data_tuples, columns=['item', 'price'])

# 엑셀로 저장하기
#df.to_csv("test.csv", mode = 'w')
df.to_csv("test.csv", mode = 'a', header=False)

# 드라이버 종료하기
driver.quit()
