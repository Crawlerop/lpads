import datetime
from mitmproxy import http
import base64

R_DB = '''role: 1
producer: 12
timestamp: [TS]
latlng {
  latitude_e7: [LE7]
  longitude_e7: [OE7]
}
radius: [R620]
provenance: 6
'''

B_RADIUS = 250

def getTS():
    s = int(datetime.datetime.now().timestamp() * 1000000)
    return s - (s % 30)

def request(rid: http.HTTPFlow):
    if rid.request.url.startswith("https://www.google.com/maps/preview/lp"):        
        tmp_url = rid.request.query["pb"].split("!")[1:]
        L_LAT, L_LNG, L_DIST = float(tmp_url[8][2:]), float(tmp_url[7][2:]), float(tmp_url[6][2:])

        UULO_DATA = base64.b64encode(
            R_DB.replace("[TS]", str(getTS())).replace("[LE7]", str(int(L_LAT*1e7))).replace("[OE7]", str(int(L_LNG*1e7))).replace("[R620]", str(int((B_RADIUS if B_RADIUS > 0 else L_DIST)*620))).encode("ascii")
        ).decode("ascii")                
        UULO_OVERRIDE = f"""a+{UULO_DATA}"""        

        rid.request.cookies["UULE"] = UULO_OVERRIDE