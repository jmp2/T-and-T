import pandas as pd
import requests

symbol = 6408 # Financial stock
resolution = 1 # Time resolution
t_start = 1664565060 # Initial time
t_final = 1664567939 # Final time

url = "https://tvc4.investing.com/25bb9d3d09dcde4f698aae33d569f7a7/1668119234/4/4/58/history?symbol=6408&resolution=1&from=1664565060&to=1664567939"

base_url = "https://tvc4.investing.com/25bb9d3d09dcde4f698aae33d569f7a7/1668119234/4/4/58/history?"

symbol_url = "symbol=" + str(symbol)
resolution_url = "&resolution=" + str(resolution)
t_start_url="&from=" + str(t_start)
t_final_url = "&to=" + str(t_final)

url = base_url + symbol_url + resolution_url + t_start_url + t_final_url

url = "https://i-invdn-com.investing.com/js/lazysizes.min.js"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Host":"tvc4.investing.com",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"none",
    "Sec-Fetch-User":"?1",
    "TE":"trailers",
    "Upgrade-Insecure-Requests":"1",
}

# cookies = {
#     "user-browser-sessions":"2",
#     "adBlockerNewUserDomains":"1667993816",
#     "udid":"de7a794805038355de945194fc11d575",
#     "_ga_C4NDLGKVMK":"GS1.1.1668119610.2.1.1668119666.4.0.0",
#     "_ga":"GA1.2.186483630.1667993817",
#     "_fbp":"fb.1.1667993818367.1949103990",
#     # "OptanonConsent":"isGpcEnabled=0&datestamp=Thu+Nov+10+2022+23%3A34%3A28+GMT%2B0100+(hora+est%C3%A1ndar+de+Europa+central)&version=6.38.0&isIABGlobal=false&hosts=&consentId=490ba67f-b6ca-4860-8848-582385dc757c&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3…_RUz371WysJm_xkpbQ; __gpi=UID=00000b1d5b5241da:T=1667993821:RT=1668119611:S=ALNI_MZZ4GeCN2TdGZoY-X12l70jHH6noA",
#     "_cc_id":"d0752ad6675676554baa5cf49e0a302c",
#     "reg_trk_ep":"exit popup banner",
#     "page_view_count":"1",
#     "pm_score":"clear",
#     "_hjSessionUser_174945":"eyJpZCI6IjEwM2VhYzljLTBkZDYtNWVlOC05MTkwLTk4NGVhYTA3MTQzZSIsImNyZWF0ZWQiOjE2NjgxMTk2NDc2OTUsImV4aXN0aW5nIjpmYWxzZX0=",
#     "__cf_bm":"3LSIJlh_PbQpLBDV1kXmzG7Kj8H3LmxslvsEvYaXY9o-1668251671-0-ASfPwTdxoN+JVXOKeFlVoboWI90mn2q4mhENgoF3ChNrlRk5gxr2d6mrIs8H4JVukSWh9wwvyZ25D0jhfnwRF7U="
# }


cookies = {
    "geoC":"ES"
}

response = requests.get(url)#, headers=headers) #,cookies=cookies)

print(response.text)
