import requests
import requests_html
from bs4 import BeautifulSoup
import json


URL = "https://shop.countdown.co.nz/api/v1/products?target=specials&page=1"
headers = {
    'authority' : 'shop.countdown.co.nz',
    'method' : 'GET',
    'path' : '/api/v1/products?target=specials&page=1',
    'scheme' : 'https',
    'accept' : 'application/json, text/plain, */*',
    'accept-encoding' : 'gzip, deflate, br',
    'accept-language' : 'en-US,en;q=0.9',
    'cache-control' : 'no-cache',
    'content-type' : 'application/json',
    'cookie' : 'AKA_A2=A; gig_bootstrap_3_-SfMo7rbUCn0p7mhjsDfYu8T5axQEv6QEEK9Edz5fo-fZombWKJzRgCf1-js9O2g=login_ver4; ARRAffinity=c2dba6f1a343c8b908c4c09af49d7b98f09d8a609f95e791c930db34ec6d2ef1; ARRAffinitySameSite=c2dba6f1a343c8b908c4c09af49d7b98f09d8a609f95e791c930db34ec6d2ef1; gig_canary=false; dtid=2:yujiBOMCabALVtd2TufrB94Z5Z5dTBTDn4T3nUNY9U15eASn90J+Bb4KgqsAjzfUEet+hLrvvT78MZ1jpHyUnBGRrHV85dLrLCbm4nKjRRSFElNVFI573SvJL7yKMy7sTAo=; ASP.NET_SessionId=grmdjmeumbrq1bp3axvcebtu; cw-laie=41716c074f124621b1e5780e4210dfef; ai_user=EsuHh|2021-03-15T08:24:53.013Z; gig_bootstrap_3_PWTq_MK-V930M4hDLpcL_qqUx224X_zPBEZ8yJeX45RHI-uKWYQC5QadqeRIfQKB=login_ver4; cw-arjshtsw=ta2d9691d536a43d5ad482f69a3220f20tbaggigsm; gig_canary_ver=11903-3-26929980; akavpau_vpshop=1615799606~id=29d2b409ccd37e2e67b58e43bbe6985b; ai_sessioncw-=HAukO|1615796693557|1615799312962.43',
    'expires' : 'Sat, 01 Jan 2000 00:00:00 GMT',
    'pragma' : 'no-cache',
    'referer': 'https://shop.countdown.co.nz/shop/specials?filters=All;All;All;true;Specials%20%26%20Great%20Prices&filters=Special;Special;Special;true;Specials%20%26%20Great%20Prices&page=1',
    'request-id' : '|4d9c0244ce7946d3979253c235ebb72d.e89d57a62a984201',
    'sec-fetch-dest' : 'empty',
    'sec-fetch-mode' : 'cors',
    'sec-fetch-site' : 'same-origin',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'x-requested-with' : 'OnlineShopping.WebApp'
}
page = requests.get(URL, headers=headers)

prods = page.text
data = json.loads(prods)

# for item in data:
#     print("Name: ", item["name"])
#     print("Price: ", item["price"])

print(json.dumps(data, indent=4))
