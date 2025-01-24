from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# ======================================================================================================================
URLS = {
    "BTC": "/html/body/div[1]/div/div/div/div[2]/div/section[2]/div/div[2]/div/table/tbody/tr[1]/td[2]/div/div/span[2]",
    "USDT": "/html/body/div[1]/div/div/div/div[2]/div/section[2]/div/div[2]/div/table/tbody/tr[2]/td[2]/div/div/span[2]",
    "ETH": "/html/body/div[1]/div/div/div/div[2]/div/section[2]/div/div[2]/div/table/tbody/tr[3]/td[2]/div/div/span[2]",
}
# ======================================================================================================================
def Digital_currency(symbol):
    url = URLS[symbol]
    driver = webdriver.Chrome()
    driver.get("https://nobitex.ir/")
    sleep(5)
    page = driver.find_element(By.XPATH, url)
    print(page.text)
    driver.quit()
Digital_currency("USDT")
# ======================================================================================================================