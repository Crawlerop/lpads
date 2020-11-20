var MAPAD_ADLIST = 0
var MAPAD_ADMAPPLACE = MAPAD_ADLIST
var MAPAD_ADNAME = 1
var MAPAD_ADLOCATION = 2
var MAPAD_ADLOCATION_PINLET = MAPAD_ADNAME
var MAPAD_ADLOCATION_PINLET_LEGACY = MAPAD_ADLOCATION
var MAPAD_ADLOCATION_PINLET_LEGACY_HI = MAPAD_ADNAME
var MAPAD_ADLOCATION_PINLET_LEGACY_IMG = MAPAD_ADLIST
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


var hex_chr = "0123456789abcdef";
function rhex(num)
{
str = "";
for(j = 0; j <= 3; j++)
str += hex_chr.charAt((num >> (j * 8 + 4)) & 0x0F) +
hex_chr.charAt((num >> (j * 8)) & 0x0F);
return str;
}
function str2blks_MD5(str)
{
nblk = ((str.length + 8) >> 6) + 1;
blks = new Array(nblk * 16);
for(i = 0; i < nblk * 16; i++) blks[i] = 0;
for(i = 0; i < str.length; i++)
blks[i >> 2] |= str.charCodeAt(i) << ((i % 4) * 8);
blks[i >> 2] |= 0x80 << ((i % 4) * 8);
blks[nblk * 16 - 2] = str.length * 8;
return blks;
}
function add(x, y)
{
var lsw = (x & 0xFFFF) + (y & 0xFFFF);
var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
return (msw << 16) | (lsw & 0xFFFF);
}
function rol(num, cnt)
{
return (num << cnt) | (num >>> (32 - cnt));
}
function cmn(q, a, b, x, s, t)
{
return add(rol(add(add(a, q), add(x, t)), s), b);
}
function ff(a, b, c, d, x, s, t)
{
return cmn((b & c) | ((~b) & d), a, b, x, s, t);
}
function gg(a, b, c, d, x, s, t)
{
return cmn((b & d) | (c & (~d)), a, b, x, s, t);
}
function hh(a, b, c, d, x, s, t)
{
return cmn(b ^ c ^ d, a, b, x, s, t);
}
function ii(a, b, c, d, x, s, t)
{
return cmn(c ^ (b | (~d)), a, b, x, s, t);
}
function hash_md5(str)
{
x = str2blks_MD5(str);
var a = 1732584193;
var b = -271733879;
var c = -1732584194;
var d = 271733878;
for(i = 0; i < x.length; i += 16)
{
var olda = a;
var oldb = b;
var oldc = c;
var oldd = d;
a = ff(a, b, c, d, x[i+ 0], 7 , -680876936);
d = ff(d, a, b, c, x[i+ 1], 12, -389564586);
c = ff(c, d, a, b, x[i+ 2], 17, 606105819);
b = ff(b, c, d, a, x[i+ 3], 22, -1044525330);
a = ff(a, b, c, d, x[i+ 4], 7 , -176418897);
d = ff(d, a, b, c, x[i+ 5], 12, 1200080426);
c = ff(c, d, a, b, x[i+ 6], 17, -1473231341);
b = ff(b, c, d, a, x[i+ 7], 22, -45705983);
a = ff(a, b, c, d, x[i+ 8], 7 , 1770035416);
d = ff(d, a, b, c, x[i+ 9], 12, -1958414417);
c = ff(c, d, a, b, x[i+10], 17, -42063);
b = ff(b, c, d, a, x[i+11], 22, -1990404162);
a = ff(a, b, c, d, x[i+12], 7 , 1804603682);
d = ff(d, a, b, c, x[i+13], 12, -40341101);
c = ff(c, d, a, b, x[i+14], 17, -1502002290);
b = ff(b, c, d, a, x[i+15], 22, 1236535329);
a = gg(a, b, c, d, x[i+ 1], 5 , -165796510);
d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632);
c = gg(c, d, a, b, x[i+11], 14, 643717713);
b = gg(b, c, d, a, x[i+ 0], 20, -373897302);
a = gg(a, b, c, d, x[i+ 5], 5 , -701558691);
d = gg(d, a, b, c, x[i+10], 9 , 38016083);
c = gg(c, d, a, b, x[i+15], 14, -660478335);
b = gg(b, c, d, a, x[i+ 4], 20, -405537848);
a = gg(a, b, c, d, x[i+ 9], 5 , 568446438);
d = gg(d, a, b, c, x[i+14], 9 , -1019803690);
c = gg(c, d, a, b, x[i+ 3], 14, -187363961);
b = gg(b, c, d, a, x[i+ 8], 20, 1163531501);
a = gg(a, b, c, d, x[i+13], 5 , -1444681467);
d = gg(d, a, b, c, x[i+ 2], 9 , -51403784);
c = gg(c, d, a, b, x[i+ 7], 14, 1735328473);
b = gg(b, c, d, a, x[i+12], 20, -1926607734);
a = hh(a, b, c, d, x[i+ 5], 4 , -378558);
d = hh(d, a, b, c, x[i+ 8], 11, -2022574463);
c = hh(c, d, a, b, x[i+11], 16, 1839030562);
b = hh(b, c, d, a, x[i+14], 23, -35309556);
a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060);
d = hh(d, a, b, c, x[i+ 4], 11, 1272893353);
c = hh(c, d, a, b, x[i+ 7], 16, -155497632);
b = hh(b, c, d, a, x[i+10], 23, -1094730640);
a = hh(a, b, c, d, x[i+13], 4 , 681279174);
d = hh(d, a, b, c, x[i+ 0], 11, -358537222);
c = hh(c, d, a, b, x[i+ 3], 16, -722521979);
b = hh(b, c, d, a, x[i+ 6], 23, 76029189);
a = hh(a, b, c, d, x[i+ 9], 4 , -640364487);
d = hh(d, a, b, c, x[i+12], 11, -421815835);
c = hh(c, d, a, b, x[i+15], 16, 530742520);
b = hh(b, c, d, a, x[i+ 2], 23, -995338651);
a = ii(a, b, c, d, x[i+ 0], 6 , -198630844);
d = ii(d, a, b, c, x[i+ 7], 10, 1126891415);
c = ii(c, d, a, b, x[i+14], 15, -1416354905);
b = ii(b, c, d, a, x[i+ 5], 21, -57434055);
a = ii(a, b, c, d, x[i+12], 6 , 1700485571);
d = ii(d, a, b, c, x[i+ 3], 10, -1894986606);
c = ii(c, d, a, b, x[i+10], 15, -1051523);
b = ii(b, c, d, a, x[i+ 1], 21, -2054922799);
a = ii(a, b, c, d, x[i+ 8], 6 , 1873313359);
d = ii(d, a, b, c, x[i+15], 10, -30611744);
c = ii(c, d, a, b, x[i+ 6], 15, -1560198380);
b = ii(b, c, d, a, x[i+13], 21, 1309151649);
a = ii(a, b, c, d, x[i+ 4], 6 , -145523070);
d = ii(d, a, b, c, x[i+11], 10, -1120210379);
c = ii(c, d, a, b, x[i+ 2], 15, 718787259);
b = ii(b, c, d, a, x[i+ 9], 21, -343485551);
a = add(a, olda);
b = add(b, oldb);
c = add(c, oldc);
d = add(d, oldd);
}
return rhex(a) + rhex(b) + rhex(c) + rhex(d);
}

function distance(lat1, lon1, lat2, lon2, unit) {
    if ((lat1 == lat2) && (lon1 == lon2)) {
        return 0;
    }
    else {
        var radlat1 = Math.PI * lat1/180;
        var radlat2 = Math.PI * lat2/180;
        var theta = lon1-lon2;
        var radtheta = Math.PI * theta/180;
        var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
        if (dist > 1) {
            dist = 1;
        }
        dist = Math.acos(dist);
        dist = dist * 180/Math.PI;
        dist = dist * 60 * 1.1515;
        if (unit=="K") { dist = dist * 1.609344 }
        if (unit=="N") { dist = dist * 0.8684 }
        return dist;
    }
}

function parseAds(lat, lng, mapad, blacklist=[], placeblacklist=[]) {
    var ret = {"noAds": false, "mapAds": null}
    var listdata = mapad[MAPAD_ADLIST]
    adId = 0
    if (typeof listdata !== "undefined" && listdata !== null) {
        ret.mapAds = []
        listdata.forEach(function(ldata){
            let granted = true
            let toofar = false
            if (blacklist.length >= 1) {
                for (i=0;i<blacklist.length;i++) {
                    if (ldata[MAPAD_ADNAME].search(blacklist[i]) != -1) {
                        granted = false
                        break
                    }
                }
            }
            if (placeblacklist.length >= 1) {
                for (i=0;i<placeblacklist.length;i++) {
                    if (ldata[MAPAD_ADMAPPLACE] == placeblacklist[i]) {
                        granted = false
                        break
                    }
                }
            }
            if (distance(lat, lng, ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLAT], ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLNG], "K") > 75) {
                granted = false
                toofar = true
            }
            if (granted == true) {
                adPlace = ldata[MAPAD_ADMAPPLACE]
                adName = ldata[MAPAD_ADNAME]
                adLocData = [ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLAT].toString(), ldata[MAPAD_ADLOCATION][MAPAD_ADLL][MAPAD_ADLOCATIONLNG].toString()]
                adUrlLink = ldata[MAPAD_ADLINKS][MAPAD_ADCLICK]
                adBaseSite = ldata[MAPAD_ADSITE][MAPAD_ADSITE_BASESITE]
                adWtaP = ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTA]
                adWta = adWtaP + ". " + ldata[MAPAD_ADSITE][MAPAD_ADSITE_WTAARRAY].join(" ")
                adPinlet = ldata[MAPAD_ADLOCATION][MAPAD_ADLOCATION_PINLET]
                if (adPinlet == null && ldata[MAPAD_ADLOCATION][MAPAD_ADLOCATION_PINLET_LEGACY] != null) { /* LPAds before smart campaigns doesn't have this feature */
                
                    adPinlet = ldata[MAPAD_ADLOCATION][MAPAD_ADLOCATION_PINLET_LEGACY][MAPAD_ADLOCATION_PINLET_LEGACY_HI][MAPAD_ADLOCATION_PINLET_LEGACY_IMG].split("?sqp=")[0]
                }
                adData = null
                if (ldata[MAPAD_ADDATA] != null) {
                    adImg = ldata[MAPAD_ADDATA][MAPAD_ADDATA_IMAGE]
                    adUrlLink = ldata[MAPAD_ADDATA][MAPAD_ADDATA_LINK]
                    adPromoTxt = ldata[MAPAD_ADDATA][MAPAD_ADDATA_PROMO]
                    adPromolyr = {"promoTitle": adPromoTxt[0], "promoDesc": adPromoTxt[1], "promoButton": adPromoTxt[2]}
                    adData = {"adImage": adImg, "adPromo": adPromolyr}
                }
                ret.mapAds.push({"adName":adName,"adPlace":adPlace,"adLocation":adLocData.join(", "),"adLink":adUrlLink,"adSite":adBaseSite,"adWhy":adWta,"promoData":adData,"adPinImage":adPinlet,"id":adId,"hash":hash_md5(adName+adBaseSite+adPlace)})
                adId++
            } else {
                if (!toofar) {
                    console.log(ldata[MAPAD_ADNAME]+": "+ldata[MAPAD_ADMAPPLACE]+" has been excluded! This ad will not be included in LPAds!")
                } else {
                    // console.log(ldata[MAPAD_ADNAME]+": "+ldata[MAPAD_ADMAPPLACE]+" is too far for ads!")
                }
            }
        })
    } else {
        ret.noAds = true
    }
    if (ret.noAds == false && ret.mapAds.length < 1) ret.noAds = true
    return ret
}
