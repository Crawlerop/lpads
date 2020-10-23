import json
import sys
import locadslib
#import yotlib as yot
# https://www.google.com/maps/preview/lp?authuser=0&hl=en&gl=id&pb=!1m3!1sDtyOX_6IDc-f9QOK7ZS4DA!7e81!15i60107!2m9!1m3!1d1!2d(lng)!3d(lat)!2m0!3m2!1i1366!2i657!4f0.1!5m2!3b0!5e11

'''
try:
    import httpx as httpapi
    hsession = httpapi.Client(http2=True)
    htimeout = httpapi.Timeout(read=900, write=900, pool=900, connect_timeout=900)
except Exception:
    import requests as httpapi
    hsession = httpapi.Session()
    adapter = httpapi.adapters.HTTPAdapter(
        pool_connections=128,
        pool_maxsize=128
    )
    hsession.mount("http://", adapter)
    hsession.mount("https://", adapter)
    htimeout = httpapi.Timeout(900)
'''

def main():
    '''
    lat = sys.argv[1]
    lng = sys.argv[2]
    '''
    o = open(sys.argv[1], "r", encoding="utf-8").read().replace(")]}'\n","")
    # print(o)
    jsfile = json.loads(o)
    mapad = locadslib.MapAds(jsfile)
    for mapa in mapad.mapads:
        print(f"Ad Name: {mapa.get('adName')}")
        print(f"Ad Location: {mapa.get('adLocation')}")
        print(f"Ad Link: {mapa.get('adLink')}")
        print(f"Ad Site: {mapa.get('adSite')}")
        print(f"Ad WTA: {mapa.get('adWhy')}")
        if mapa.get('promoData'):
            print(f"Have Promo: yes")
        else:
            print(f"Have Promo: no")

    # open("dump_d", "w", encoding="utf-8").write(json.dumps(mapad.mapads))
    
    


if __name__ == "__main__":
    main()