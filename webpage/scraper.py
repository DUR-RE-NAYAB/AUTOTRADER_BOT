import requests
from bs4 import BeautifulSoup
# url = "https://www.autotrader.ca/cars/on/toronto/?rcp=1000000&rcs=0&srt=35&prx=250&prv=Ontario&loc=Toronto%2C%20ON&hprc=True&wcp=True&inMarket=advancedSearch"
def scrape_data():
    payload = {}
    headers = {
    'authority': 'www.autotrader.ca',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,en-US;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'atOptUser=be57b031-9a3d-4357-ad55-752c1437adce; visid_incap_820541=jHnrRGy7Si63bY7znvyMfz0J0WQAAAAAQUIPAAAAAACbQW/uefdA1Jzq/aykVP9C; incap_ses_1234_820541=4l55JNLGwh2wvq04kgwgET0J0WQAAAAAmEpMkXenu9eFS/QnQVa2Ug==; optimizelyEndUserId=oeu1691420916689r0.7266951875226633; cbnr=1; gcl_au=1.1.823052818.1691420917; srchLocation=%7B%22Location%22%3A%7B%22Address%22%3Anull%2C%22City%22%3A%22Toronto%22%2C%22Latitude%22%3A43.70011%2C%22Longitude%22%3A-79.4163%2C%22Province%22%3A%22ON%22%2C%22PostalCode%22%3Anull%2C%22Type%22%3A%22%22%7D%2C%22UnparsedAddress%22%3A%22Toronto%2C%20ON%22%7D; {E7ABF06F-D6A6-4c25-9558-3932D3B8A04D}=; PageSize=15; _gid=GA1.2.1605810181.1691420918; __GTMADBLOCKER=no; _pbjs_userid_consent_data=3524755945110770; sa-user-id=s%253A0-0eee113d-2712-5859-79f8-f91f5d994cd3.RmsjuZhmwdUGmW1CdhSjX8Q4EsY%252BKcDhmOf%252BRlQZHKw; sa-user-id-v2=s%253ADu4RPScSWFl5-PkfXZlM029YWqc.sOmyTmdaTRFRYjRNBn22HLaBaq76sPjQC7XbmqNeIiU; sa-user-id-v3=s%253AAQAKIJLQX92E6uraKQ8LkCejwCOk8pjrDjRtxP1ChNMxh5KZEHwYBCC48bOlBjABOgSp83QWQgQT3a95.KQRCKF9WefPL6EIBsUOw0wel5hfP%252FE8oKWicAFEeiCY; _fbp=fb.1.1691420918716.1913764679; _clck=mle68s|2|fdy|0|1314; _cc_id=b84e168894816412237b314f9b46d746; panoramaId=802bde05e5120a5b11231992103a4945a7029dfc92094f2590e72f2b4288d0ab; panoramaIdType=panoIndiv; cc_audpid=b84e168894816412237b314f9b46d746; _pin_unauth=dWlkPVkyRmtOell3WVRZdFpqUmtOeTAwWVdJeExUbGhabUV0TnpSaVpqVTRPR0ZtTnpGaQ; _tt_enable_cookie=1; _ttp=Q02opGtACOgw8gNfv3VWj97n49p; tgcid=830473746.1691420918; __qca=P0-1573945792-1691420920440; searchState={"isUniqueSearch":false,"make":null,"model":null}; nlbi_820541_1646237=QXE+E7Q6qiYN+2IsrnsxyAAAAAABGDRQ1FDgL88ojVKY0A4n; SortOrder=BoostDesc; __T2CID_=fd6a9cc0-6cd9-4030-9269-9f4458e849cd; searchBreadcrumbs=%7B%22srpBreadcrumb%22%3A%5B%7B%22Text%22%3A%22Cars%2C%20Trucks%20%26%20SUVs%22%2C%22Url%22%3A%22%2Fcars%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%2C%7B%22Text%22%3A%22Ontario%22%2C%22Url%22%3A%22%2Fcars%2Fon%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%2C%7B%22Text%22%3A%22Toronto%22%2C%22Url%22%3A%22%2Fcars%2Fon%2Ftoronto%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%5D%2C%22isFromSRP%22%3Afalse%2C%22neighbouringIds%22%3Anull%7D; incap_ses_961_820541=DIlse7ZMZEz1nkYXXSlWDfUN0WQAAAAAM7gQN6N9yMT51hp4W2An2A==; _uetsid=49a7c700353411ee9803137614d78298; _uetvid=49a7e590353411ee8b8675325e2769bd; _ga=GA1.2.830473746.1691420918; _derived_epik=dj0yJnU9Q3N1TEhOanQ1ZEJEb080X0czVW9kU0ZleFBVOUdyS1Imbj1FRzdFc2otcWQwT1NQZEFjdEQtYXFRJm09MSZ0PUFBQUFBR1RSRGZnJnJtPTEmcnQ9QUFBQUFHVFJEZmcmc3A9Mg; _td=094c7238-1847-4f31-919c-d1b1f1f0d837; cto_bundle=LymnlV9pcjNaMHVVbkdYWmlja1JKTThJSHZXZnFMJTJGYlY5cHdIaUU4Z3gxZ1NNdlFVM1lRQUtmRnp6RWMlMkZJdlNKd2VtaE16TTFMWm5qJTJGc09tQkg4dW9YY3BBdTBPdGl2N3J6emM0JTJGcW45Sk8lMkJkN3dSQlY3cDNyVUlEZzcxOGJpWFQwNUdZZjJOU2c4RENYUmsxcFFOZU1jOUVRJTNEJTNE; __gads=ID=8d540d300ac89034:T=1691420994:RT=1691422203:S=ALNI_MaDaAf5h2ch0DagGoaiQMYqHekZfg; __gpi=UID=00000c7a2d2abdbb:T=1691420994:RT=1691422203:S=ALNI_MbqnWrPgdC8LgCcsaro5_VV9Ba4Pg; lastsrpurl=/cars/on/toronto/?rcp=15&rcs=15&srt=35&prx=250&prv=Ontario&loc=Toronto%2C%20ON&hprc=True&wcp=True&inMarket=advancedSearch; _ga_PCMZZ2EWK8=GS1.1.1691420918.1.1.1691422133.52.0.0; panoramaId_expiry=1692027007541; _clsk=so4x59|1691422133585|8|0|s.clarity.ms/collect; _gali=wrapper; atOptUser=be57b031-9a3d-4357-ad55-752c1437adce; nlbi_820541_1646237=pU+9ZnPfyBo5gTAQrnsxyAAAAAAE4A4RpqjA5m6GSd+9M2lW; searchBreadcrumbs=%7B%22srpBreadcrumb%22%3A%5B%7B%22Text%22%3A%22Cars%2C%20Trucks%20%26%20SUVs%22%2C%22Url%22%3A%22%2Fcars%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%2C%7B%22Text%22%3A%22Ontario%22%2C%22Url%22%3A%22%2Fcars%2Fon%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%2C%7B%22Text%22%3A%22Toronto%22%2C%22Url%22%3A%22%2Fcars%2Fon%2Ftoronto%2F%3Fsrt%3D35%26prv%3DOntario%26loc%3DToronto%252C%2520ON%26hprc%3DTrue%26wcp%3DTrue%22%7D%5D%2C%22isFromSRP%22%3Afalse%2C%22neighbouringIds%22%3Anull%7D',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    lst = []
    # offset = 0
    # limit = 100
    # response = {} ,{'a'}
    offset, limit = 0,100
    count = 0
    for i in range(10000000):
        url = f"https://www.autotrader.ca/cars/on/toronto/?rcp={limit}&rcs={offset}&srt=35&prx=250&prv=Ontario&loc=Toronto%2C%20ON&hprc=True&wcp=True&inMarket=advancedSearch"
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.text and count <= 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            datas = soup.find_all('span', class_='title-with-trim')
            
            for data in datas:
                lst.append(data.text)
                count += 1
        else:
            break
        offset += limit
    return lst
