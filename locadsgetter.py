import json
import sys
import locadslib
import time
import datetime
import base64
#import yotlib as yot
# https://www.google.com/maps/preview/lp?authuser=0&hl=en&gl=id&pb=!1m3!1sDtyOX_6IDc-f9QOK7ZS4DA!7e81!15i60107!2m9!1m3!1d1!2d(lng)!3d(lat)!2m0!3m2!1i1366!2i657!4f0.1!5m2!3b0!5e11

#PROXY_SITE = "http://localhost:8080"
PROXY_SITE = ""

template = '''
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />

                <link rel="stylesheet" href="https://unpkg.com/leaflet@latest/dist/leaflet.css" crossorigin=""/>
                <script src="https://unpkg.com/leaflet@latest/dist/leaflet.js" crossorigin=""></script>
                <style>
                    body {
                        padding: 0;
                        margin: 0;
                    }
                    html, body, #mapid {
                        height: 100%;
                        width: 100%;
                    }
                    textarea.righttext {
                        position:absolute;
                        right:1px;
                        bottom:15px;
                        resize:none;
                    }
                    button.rightbutton {
                        position:absolute;
                        right:1px;
                        bottom:15px;
                        resize:none;
                    }
                </style>
                
            </head>
            <body>
                <div id="mapid"></div>
                <script>
                    var data = L.layerGroup()
                    var adData = (ADDATA)

                    mapboxattr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' + '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>'

                    gmapsattr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' + '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery © <a href="https://maps.google.com/">Google Maps</a>'

                    esriattr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' + '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery © <a href="https://www.esri.com/">ESRI</a>'
                    
                    osmattr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'

                    normal = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                        maxZoom: 21,
                        attribution: mapboxattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 512,
                        zoomOffset: -1
                    })

                    mdefault = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                        maxZoom: 21,
                        attribution: mapboxattr,
                        id: 'mapbox/streets-v11',
                        tileSize: 512,
                        zoomOffset: -1
                    })

                    mgray = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                        maxZoom: 21,
                        attribution: mapboxattr,
                        id: 'mapbox/light-v9',
                        tileSize: 512,
                        zoomOffset: -1
                    })

                    esrinormal = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
                        maxZoom: 21,
                        attribution: esriattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    esriterrain = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
                        maxZoom: 21,
                        attribution: esriattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        maxZoom: 21,
                        attribution: osmattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    satellite = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                        maxZoom: 21,
                        attribution: mapboxattr,
                        id: 'user12435235124125235824592457/ckanekpxi1o3y1ipkm8tl6v3i',
                        tileSize: 512,
                        zoomOffset: -1
                    })

                    satellitenotext = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
                        maxZoom: 21,
                        attribution: mapboxattr,
                        id: 'user12435235124125235824592457/ckb7ik2nf4rel1ip61enm2h23',
                        tileSize: 512,
                        zoomOffset: -1
                    })

                    gmapsnormal = L.tileLayer('https://www.google.com/maps/vt/pb=!1m4!1m3!1i{z}!2i{x}!3i{y}!2m1!1i0!3m2!2sen-US!5i1106!5m1!5f4.0!23i1358902', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    gmapsvue = L.tileLayer('https://maps.googleapis.com/maps/vt?pb=!1m5!1m4!1i{z}!2i{x}!3i{y}!4i256!2m3!1e0!2sm!3i520236120!3m17!2sen-US!3sUS!5e18!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!12m4!1e26!2m2!1sstyles!2zcy50OjF8cy5lOmwudC5mfHAuYzojZmY0NDQ0NDQscy50OjV8cC5jOiNmZmYyZjJmMixzLnQ6MnxwLnY6b2ZmLHMudDozfHAuczotMTAwfHAubDo0NSxzLnQ6NDl8cC52OnNpbXBsaWZpZWQscy50OjUwfHMuZTpsLml8cC52Om9mZixzLnQ6NHxwLnY6b2ZmLHMudDo2fHAuYzojZmYyNjJlNDV8cC52Om9uLHMudDo2fHMuZTpsfHAudjpvZmY!4e0!5m1!5f4.0', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    gmapsfb = L.tileLayer('https://maps.googleapis.com/maps/vt?pb=!1m5!1m4!1i{z}!2i{x}!3i{y}!4i256!2m3!1e0!2sm!3i520236108!3m17!2sen-US!3sUS!5e18!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!12m4!1e26!2m2!1sstyles!2zcy5lOmwuaXxwLnY6b2ZmLHMudDoxfHAudjpvbixzLnQ6NXxwLmM6I2ZmZThlOWU5LHMudDoyfHMuZTpnfHAuYzojZmZlOGU5ZTkscy50OjQwfHAuYzojZmZiYWQyOTQscy50OjQwfHMuZTpsfHAudjpvZmYscy50OjQ5fHMuZTpnLmZ8cC5jOiNmZmZmZmZmZixzLnQ6NDl8cy5lOmcuc3xwLnY6b2ZmLHMudDo1MHxzLmU6Zy5mfHAuYzojZmZmZmZmZmYscy50OjUwfHMuZTpnLnN8cC52Om9mZixzLnQ6NTF8cy5lOmcuZnxwLmM6I2ZmZmJmYmZiLHMudDo0fHAudjpvZmYscy50OjZ8cy5lOmd8cC5jOiNmZjQxYWVjOSxzLnQ6NnxzLmU6bC50LmZ8cC5jOiNmZjA2NTk3MSxzLnQ6NnxzLmU6bC50LnN8cC52OnNpbXBsaWZpZWQ!4e0!5m1!5f4.0', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    gmapsgray = L.tileLayer('https://maps.googleapis.com/maps/vt?pb=!1m5!1m4!1i{z}!2i{x}!3i{y}!4i256!2m3!1e0!2sm!3i520233372!3m17!2sen-US!3sUS!5e18!12m4!1e68!2m2!1sset!2sRoadmap!12m3!1e37!2m1!1ssmartmaps!12m4!1e26!2m2!1sstyles!2zcy50OjZ8cy5lOmd8cC5jOiNmZmU5ZTllOXxwLmw6MTcscy50OjV8cy5lOmd8cC5jOiNmZmY1ZjVmNXxwLmw6MjAscy50OjQ5fHMuZTpnLmZ8cC5jOiNmZmZmZmZmZnxwLmw6MTcscy50OjQ5fHMuZTpnLnN8cC5jOiNmZmZmZmZmZnxwLmw6Mjl8cC53OjAuMixzLnQ6NTB8cy5lOmd8cC5jOiNmZmZmZmZmZnxwLmw6MTgscy50OjUxfHMuZTpnfHAuYzojZmZmZmZmZmZ8cC5sOjE2LHMudDoyfHMuZTpnfHAuYzojZmZmNWY1ZjV8cC5sOjIxLHMudDo0MHxzLmU6Z3xwLmM6I2ZmZGVkZWRlfHAubDoyMSxzLmU6bC50LnN8cC52Om9ufHAuYzojZmZmZmZmZmZ8cC5sOjE2LHMuZTpsLnQuZnxwLnM6MzZ8cC5jOiNmZjMzMzMzM3xwLmw6NDAscy5lOmwuaXxwLnY6b2ZmLHMudDo0fHMuZTpnfHAuYzojZmZmMmYyZjJ8cC5sOjE5LHMudDoxfHMuZTpnLmZ8cC5jOiNmZmZlZmVmZXxwLmw6MjAscy50OjF8cy5lOmcuc3xwLmM6I2ZmZmVmZWZlfHAubDoxN3xwLnc6MS4y!4e0!5m1!5f4.0', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    gmapsbold = L.tileLayer('https://www.google.com/maps/vt?pb=!1m4!1m3!1i{z}!2i{x}!3i{y}!2m2!2sm!3i504221335!3m7!2sen-US!5i1105!12m4!1i68!2m2!1sset!2sTerrain!5m1!5f4.0!23i1358902', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    esrisatellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
                        maxZoom: 21,
                        attribution: esriattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })                    

                    esrisatellitealt = L.tileLayer('https://clarity.maptiles.arcgis.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
                        maxZoom: 21,
                        attribution: esriattr,
                        id: 'user12435235124125235824592457/ckao1rqf85kh01imwyf5b0pvc',
                        tileSize: 256,
                        zoomOffset: 0
                    })

                    gmapssatellite = L.tileLayer('https://mt{s}.googleapis.com/vt?lyrs=y&hl=en-US&x={x}&y={y}&z={z}', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckanekpxi1o3y1ipkm8tl6v3i',
                        tileSize: 256,
                        zoomOffset: 0,
                        subdomains: ["0", "1", "2", "3"]
                    })

                    gmapssatellitenotext = L.tileLayer('https://mt{s}.googleapis.com/vt?lyrs=s&hl=en-US&x={x}&y={y}&z={z}', {
                        maxZoom: 21,
                        attribution: gmapsattr,
                        id: 'user12435235124125235824592457/ckanekpxi1o3y1ipkm8tl6v3i',
                        tileSize: 256,
                        zoomOffset: 0,
                        subdomains: ["0", "1", "2", "3"]
                    })

                    blank = L.tileLayer('http://nope', {
                        maxZoom: 21,
                        attribution: "",
                        tileSize: 256,
                        zoomOffset: 0,
                    })

                    var mymap = L.map('mapid', {
                        center: adData.startLocation.split(", "),
                        zoom: 14,
                        layers: [normal, data]
                    })

                    var layernames = {
                        "Mapbox Normal": normal,
                        "Mapbox Streets": mdefault,
                        "Mapbox Grayscale": mgray,
                        "Google Maps Normal": gmapsnormal,
                        "Google Maps Normal (Better)": gmapsfb,
                        "Google Maps Bold": gmapsbold,
                        "Google Maps Vue": gmapsvue,
                        "Google Maps Grayscale": gmapsgray,
                        "OSM": osm,
                        "ESRI Normal": esrinormal,
                        "ESRI Terrain": esriterrain,
                        "Mapbox Satellite": satellite,
                        "Mapbox Satellite (no label)": satellitenotext,
                        "Google Maps Satellite": gmapssatellite,
                        "Google Maps Satellite (no label)": gmapssatellitenotext,
                        "ESRI Satellite": esrisatellite,
                        "ESRI Satellite (alt)": esrisatellitealt,
                        "Empty Tile": blank,
                    }
                    
                
                    layers = L.control.layers(layernames, {"Local Ads": data})
                    layers.addTo(mymap)	

                    adData.adList.forEach(function(ad){
                        m = L.marker(ad.adLocation.split(", "), {title: ad.adName})
                        adTextData = "<h1>"+ad.adName+"</h1>"
                        if (ad.promoData == null) {
                            adTextData += "Why: <b>"+ad.adWhy+"</b>"
                            adTextData += "<br><br><a href=\\""+ad.adLink+"\\">"+ad.adSite+"</a>"
                        } else {
                            adTextData = "<h1>"+ad.promoData.adPromo.promoTitle+"</h1>"
                            adTextData += "<h2>"+ad.adName+"</h2>"
                            adTextData += "<h3>"+ad.promoData.adPromo.promoDesc+"</h3>"
                            adTextData += "Why: <b>"+ad.adWhy+"</b>"
                            adTextData += "<br><br><a href=\\""+ad.adLink+"\\">"+ad.promoData.adPromo.promoButton+"</a>"
                        }
                        
                        
                        m.bindPopup(adTextData)
                        m.addTo(data)
                    })


                </script>
            </body>
        </html>
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


def main():
    global PROXY_SITE
    OUTP = None
    loadani_chars = ["/","-","\\","|"]
    lat = sys.argv[1]
    lng = sys.argv[2]
    failnoad = False
    if len(sys.argv) > 3:
        if sys.argv[3] == "-noadsfail":
            failnoad = True
        elif sys.argv[3] == "-proxy":
            PROXY_SITE = sys.argv[4]
        elif sys.argv[3] == "-outp":
            OUTP = sys.argv[4]
    if (PROXY_SITE and len(sys.argv) > 5) or (len(sys.argv) > 4):
        if PROXY_SITE:
            if sys.argv[5] == "-noadsfail":
                failnoad = True
            elif sys.argv[5] == "-proxy":
                PROXY_SITE = sys.argv[6]
            elif sys.argv[5] == "-outp":
                OUTP = sys.argv[6]
        else:
            if sys.argv[4] == "-noadsfail":
                failnoad = True
            elif sys.argv[4] == "-proxy":
                PROXY_SITE = sys.argv[5]
            elif sys.argv[4] == "-outp":
                OUTP = sys.argv[5]
    if (PROXY_SITE and len(sys.argv) > 6) or (len(sys.argv) > 5):
        if PROXY_SITE:
            if sys.argv[6] == "-noadsfail":
                failnoad = True
            elif sys.argv[6] == "-proxy":
                PROXY_SITE = sys.argv[7]
            elif sys.argv[6] == "-outp":
                OUTP = sys.argv[7]
        else:
            if sys.argv[5] == "-noadsfail":
                failnoad = True
            elif sys.argv[5] == "-proxy":
                PROXY_SITE = sys.argv[6]
            elif sys.argv[5] == "-outp":
                OUTP = sys.argv[6]
    
    # print(OUTP)

    mapad = locadslib.MapAds([None])
    startloc = f"{lat}, {lng}"
    tick = time.perf_counter()+0.05
    lt = 0
    print(f"Searching ads for {lat}, {lng}... [{loadani_chars[lt]}]", end="\r")
    while mapad.noads:
        if time.perf_counter() >= tick:
            lt += 1
            if lt > 3:
                lt = 0
            print(f"Searching ads for {lat}, {lng}... [{loadani_chars[lt]}]", end="\r")
        if PROXY_SITE:
            hapi = httpapi.get(f"https://www.google.com/maps/preview/lp?authuser=0&hl=en&gl=us&pb=!1m3!1s0!7e81!15i60107!2m9!1m3!1d1!2d{lng}!3d{lat}!2m0!3m2!1i4096!2i2048!4f14!5m2!3b0!5e11", timeout=htimeout, proxies={"http":PROXY_SITE,"https":PROXY_SITE})
        else:
            hapi = httpapi.get(f"https://www.google.com/maps/preview/lp?authuser=0&hl=en&gl=us&pb=!1m3!1s0!7e81!15i60107!2m9!1m3!1d1!2d{lng}!3d{lat}!2m0!3m2!1i4096!2i2048!4f14!5m2!3b0!5e11", timeout=htimeout)
        hapi.raise_for_status()
        
        o = hapi.content.decode("utf-8").replace(")]}'\n","")
        jsfile = json.loads(o)
        mapad = locadslib.MapAds(jsfile)
        if mapad.noads and failnoad:
            print()
            print(f"No ad found for {lat}, {lng}!")
            hsession.cookies.clear() # prevent TFA floodgates
            sys.exit(0)

    print()
    print("Ad Found!")

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
    
    
    htmldata = json.dumps({"startLocation": startloc, "adList": mapad.mapads})
    outtemp = template.replace("(ADDATA)", htmldata)

    if not OUTP:
        if PROXY_SITE:
            outfn = f"mapad_px_{base64.encodebytes(PROXY_SITE.encode('utf-8')).decode('utf-8')[:-1]}_{base64.encodebytes(startloc.encode('utf-8')).decode('utf-8')[:-1]}_{datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')}.html"
        else:
            outfn = f"mapad_{base64.encodebytes(startloc.encode('utf-8')).decode('utf-8')[:-1]}_{datetime.datetime.now().strftime('%y-%m-%d_%H-%M-%S')}.html"
    else:
        outfn = OUTP

    open(outfn, "w", encoding="utf-8").write(outtemp)
    #open("htmldump", "w", encoding="utf-8").write(htmldata)
    #open("dump", "w", encoding="utf-8").write(json.dumps(mapad.mapads))
    hsession.cookies.clear() # prevent TFA floodgates
    
    


if __name__ == "__main__":
    main()