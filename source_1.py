import requests
from bs4 import BeautifulSoup
# ======================================================================================================================
URLS={
    "dollar":"https://www.tgju.org/profile/price_dollar_rl",
    "gold":"https://www.tgju.org/profile/geram18",
    "quarter":"https://www.tgju.org/profile/rob",
    "emami_coin":"https://www.tgju.org/profile/sekee"
}
# ======================================================================================================================
def inquiry(symbol):
    url=URLS[symbol]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    spans=soup.find_all("span",class_="value")
    spans_value=str(spans[0]).split()[3]
    price=spans_value.split(">")[1].split("<")[0]
    print(50 * "*")
    print(f"{url} price :",price)
    print(50 * "*")
# ======================================================================================================================
inquiry("dollar")
# ======================================================================================================================