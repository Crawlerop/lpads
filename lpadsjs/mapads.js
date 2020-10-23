var MAPAD_ADLIST = 0
var MAPAD_ADNAME = 1
var MAPAD_ADLOCATION = 2
var MAPAD_ADLOCATIONLAT = MAPAD_ADLOCATION
var MAPAD_ADLOCATIONLNG = 3
var MAPAD_ADDATA = MAPAD_ADLOCATIONLNG
var MAPAD_ADDATA_IMAGE = MAPAD_ADLIST
var MAPAD_ADDATA_LINK = 4
var MAPAD_ADDATA_BASESITE = 5
var MAPAD_ADDATA_PROMO = 7
var MAPAD_ADLL = MAPAD_ADLIST
var MAPAD_ADLINKS = MAPAD_ADDATA_LINK
var MAPAD_ADCLICK = MAPAD_ADNAME
var MAPAD_ADSITE = MAPAD_ADDATA_BASESITE
var MAPAD_ADSITE_BASESITE = MAPAD_ADLL
var MAPAD_ADSITE_WTA = MAPAD_ADNAME
var MAPAD_ADSITE_WTAARRAY = MAPAD_ADLOCATIONLNG

function parseAds(mapad) {
    var ret = {"noAds": false, "mapAds": null}
    var listdata = mapad[MAPAD_ADLIST]
    if (listdata !== null) {
        ret.mapAds = []
        listdata.forEach(function(ldata){
            adName = ldata[MAPAD_ADNAME]
            adLocData = [ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLAT].toString(), ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLNG].toString()]
            adUrlLink = ldata[MAPAD_ADLINKS][MAPAD_ADCLICK]
            adBaseSite = ldata[MAPAD_ADSITE][MAPAD_ADSITE_BASESITE]
            adWtaP = ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTA]
            adWta = adWtaP + ". " + ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTAARRAY].join(" ")
            adData = null
            if (ldata[MAPAD_ADDATA] != null) {
                adImg = ldata[MAPAD_ADDATA][MAPAD_ADDATA_IMAGE]
                adUrlLink = ldata[MAPAD_ADDATA][MAPAD_ADDATA_LINK]
                adPromoTxt = ldata[MAPAD_ADDATA][MAPAD_ADDATA_PROMO]
                adPromolyr = {"promoTitle": adPromoTxt[0], "promoDesc": adPromoTxt[1], "promoButton": adPromoTxt[2]}
                adData = {"adImage": adImg, "adPromo": adPromolyr}
            }
            ret.mapAds.push({"adName":adName,"adLocation":adLocData.join(", "),"adLink":adUrlLink,"adSite":adBaseSite,"adWhy":adWta,"promoData":adData})
        })
    } else {
        ret.noAds = true
    }
    return ret
}