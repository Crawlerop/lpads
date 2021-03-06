'''
Library for parsing GMaps Location ads
'''

MAPAD_ADLIST = 0
MAPAD_ADMAPPLACE = MAPAD_ADLIST
MAPAD_ADNAME = 1
MAPAD_ADLOCATION = 2
MAPAD_ADLOCATION_PINLET = MAPAD_ADNAME
MAPAD_ADLOCATIONLAT = MAPAD_ADLOCATION
MAPAD_ADLOCATIONLNG = 3
MAPAD_ADDATA = MAPAD_ADLOCATIONLNG
MAPAD_ADDATA_IMAGE = MAPAD_ADLIST
MAPAD_ADDATA_LINK = 4
MAPAD_ADDATA_BASESITE = 5
MAPAD_ADDATA_PROMO = 7
MAPAD_ADLL = MAPAD_ADLIST
MAPAD_ADLINKS = MAPAD_ADDATA_LINK
MAPAD_ADCLICK = MAPAD_ADNAME
MAPAD_ADSITE = MAPAD_ADDATA_BASESITE
MAPAD_ADSITE_BASESITE = MAPAD_ADLL
MAPAD_ADSITE_WTA = MAPAD_ADNAME
MAPAD_ADSITE_WTAARRAY = MAPAD_ADLOCATIONLNG

class MapAds():
    def __init__(self, mapad: list):
        self.noads = False
        self.mapads = None
        
        listdata = mapad[MAPAD_ADLIST]
        if listdata:
            self.mapads = []
            for ldata in listdata:
                adplace = ldata[MAPAD_ADMAPPLACE]
                adname = ldata[MAPAD_ADNAME]
                adlocdata = (str(ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLAT]), str(ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLNG]))
                adurllink = ldata[MAPAD_ADLINKS][MAPAD_ADCLICK]
                adbasesite = ldata[MAPAD_ADSITE][MAPAD_ADSITE_BASESITE]
                adwtap = ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTA]
                if len(ldata[MAPAD_ADLOCATION]) > 1:
                    adpinlet = ldata[MAPAD_ADLOCATION][MAPAD_ADLOCATION_PINLET]
                else:
                    adpinlet = None
                adwta = adwtap + ". "
                adwtaterms = []
                for ls in ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTAARRAY]:
                    adwtaterms.append(ls[0])
                adwta +=  " ".join(adwtaterms)
                addata = None

                if ldata[MAPAD_ADDATA]:
                    adimg = ldata[MAPAD_ADDATA][MAPAD_ADDATA_IMAGE]
                    adurllink = ldata[MAPAD_ADDATA][MAPAD_ADDATA_LINK]
                    adpromotxt = ldata[MAPAD_ADDATA][MAPAD_ADDATA_PROMO]
                    adpromolyr = {"promoTitle": adpromotxt[0], "promoDesc": adpromotxt[1], "promoButton": adpromotxt[2]}
                    addata = {"adImage": adimg, "adPromo": adpromolyr}


                self.mapads.append({"adName":adname,"adPlace":adplace,"adLocation":", ".join(adlocdata),"adLink":adurllink,"adSite":adbasesite,"adWhy":adwta,"promoData":addata,"adPinImage":adpinlet})

        else:
            self.noads = True
