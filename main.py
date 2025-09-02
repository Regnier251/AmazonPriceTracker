import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.mx/Acer-America-Corp-Gaming-Monitor/dp/B0C1T35BCF/ref=pd_rhf_dp_s_ci_mcx_mr_hp_d_d_sccl_1_9/131-5489028-8592543?psc=1"
response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("$")[1]

print(price_without_currency)