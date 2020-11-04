var mymap = L.map('map').setView([0, 0], 2);
var xhr = new XMLHttpRequest();
var lpadURL = "https://www.google.com/maps/preview/lp?authuser=0&hl=en&gl=us&pb=!1m3!1s0!7e81!15i60107!2m9!1m3!1d(dist)!2d(long)!3d(lat)!2m0!3m2!1i32767!2i32767!4f14!5m2!3b0!5e11"
var adData = null;
var selData = null;
var index = null;
var pins = [];
var repdata = [];
var dist = 1;

up = new URLSearchParams(window.location.search)
var here = false

if (up.get("here") == "true") {
    here = true
}

if (up.get("override") != null) {
    try {
        repdata = JSON.parse(window.atob(up.get("override"))).overrides
    } catch (e) {

    }
}

if (here) {
    L.tileLayer('https://{s}.base.maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{z}/{x}/{y}/512/png?apiKey=y1jXMiseAmIRhdY2pdC5ClWFnBlNP1U_xKDns2jXtYY&lg=eng', {
    maxZoom: 19,
    subdomains: "1234",
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://wego.here.com/">HERE</a>',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);
} else {
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 21,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);
}

function jsonCopy(json) {
    return JSON.parse(JSON.stringify(json))
}

function overrideIndex(adData) {
    i = 0
    for (s = 0; s<repdata.length; s++) {
        c = repdata[s]
        if (adData.id == c.new.id) {
            return i
        }
        i += 1
    }
    return -1
}

function findOverride(adData) {
    i = 0
    for (s = 0; s<repdata.length; s++) {
        c = repdata[s]
        if (adData.id == c.target.id) {
            return i
        }
        i += 1
    }
    return -1
}

function loadMarker(data) {
    data.forEach(function(ad){
        m = L.marker(ad.adLocation.split(", "))
        if (ad.adPinImage != null) {
            m = L.marker(ad.adLocation.split(", "), {
                icon: L.icon({
                    iconUrl: ad.adPinImage,
                    iconSize: [32,32]
                })
            })
        }
        m.on("click", function(){
            index = jsonCopy(ad.id)
            selData = jsonCopy(ad)
            document.getElementById("place").value = selData.adName
            document.getElementById("location").value = selData.adLocation
            document.getElementById("host").value = selData.adSite
            document.getElementById("link").value = selData.adLink
            if (selData.adPinImage != null) {
                document.getElementById("pinlet").value = selData.adPinImage
            } else {
                document.getElementById("pinlet").value = ""
            }
            document.getElementById("wta").value = selData.adWhy
            if (selData.promoData != null) {
                document.getElementById("promo").value = JSON.stringify(selData.promoData)
            } else {
                document.getElementById("promo").value = ""
            }
            if (selData.adTown != null) {
                document.getElementById("town").value = selData.adTown
            } else {
                document.getElementById("town").value = ""
            }
        })
        pins.push(m)
        m.addTo(mymap)
    })
}

function start() {
    if (up.get('dist')) {
        dist = parseFloat(up.get('dist'))
    }
    if (up.get('lat') && up.get('lng')) {
        mymap.setView([parseFloat(up.get('lat')), parseFloat(up.get('lng'))], 14)
        xhr.open("GET", "https://api.allorigins.win/raw?url=" + encodeURIComponent(lpadURL.replace("(dist)", dist).replace("(long)", up.get("lng")).replace("(lat)", up.get("lat"))))
        xhr.onreadystatechange = function() {
            if (this.readyState == 4) {
                out = xhr.responseText.replace(")]}'\n", "")
                try {
                    adProto = JSON.parse(out)
                } catch (e) {
                    return
                }
                adResp = parseAds(adProto)
                if (adResp.noAds == true) {
                    console.warn("No ads found on "+up.get('lat')+", "+up.get('lng')+"!")
                    setTimeout(start, 200)
                } else {
                    adData = adResp.mapAds
                    if (up.get("override") != null) {
                        newData = []
                        adData.forEach(function(d){
                            ovr = findOverride(d)
                            if (ovr != -1) {
                                newData.push(jsonCopy(repdata[ovr].new)) 
                                console.log("Override found!")           
                            } else {
                                newData.push(jsonCopy(d))
                            }
                        })
                        loadMarker(newData)
                    } else {
                        loadMarker(adData)
                    }
                }
            }
        }
        xhr.send()
    }
}

start()

document.getElementById("save").onclick = function() {
    if (repdata.length > 0) {
        window.location = "mapads_marker.html?localads=true&lat="+up.get("lat")+"&lng="+up.get("lng")+"&override="+window.btoa(JSON.stringify({"overrides": repdata}))
    }
}

document.getElementById("cancel").onclick = function() {
    history.back()
}

document.getElementById("remove").onclick = function() {
    if (selData != null) {
        if (overrideIndex(selData) != -1) {
            repdata.splice(overrideIndex(selData), 1)
            alert("Data removed!")
            upd()
        }
    } 
}

document.getElementById("reload").onclick = function() {
    location.reload()
}

setInterval(() => {
    if (selData != null) {
        selData.adName = document.getElementById("place").value
        selData.adLocation = document.getElementById("location").value
        selData.adSite = document.getElementById("host").value
        selData.adLink = document.getElementById("link").value
        if (document.getElementById("town").value != "") {
            selData.adTown = document.getElementById("town").value
        } else {
            selData.adTown = undefined
        }
        if (document.getElementById("pinlet").value != "") {
            selData.adPinImage = document.getElementById("pinlet").value
        } else {
            selData.adPinImage = null
        }
        selData.adWhy = document.getElementById("wta").value
        if (document.getElementById("promo").value != "") {
            selData.promoData = JSON.parse(document.getElementById("promo").value)
        } else {
            selData.promoData = null
        }    
    }
}, 25);

document.getElementById("add").onclick = function() {
    if (selData != null) {
        ov = overrideIndex(selData)
        if (ov == -1) {
            repdata.push({"target": adData[index], "new": selData})
        } else {
            repdata[ov] = {"target": adData[index], "new": selData}
        }
        alert("Added")
        upd()
    }
}

function upd() {
    newData = []

    adData.forEach(function(d){
        ovr = findOverride(d)
        if (ovr != -1) {
            newData.push(jsonCopy(repdata[ovr].new)) 
            console.log("Override found!")           
        } else {
            newData.push(jsonCopy(d))
        }
    })
    pins.forEach(function(a){
        a.remove()
    })
    selData = null
    document.getElementById("place").value = ""
    document.getElementById("location").value = ""
    document.getElementById("host").value = ""
    document.getElementById("link").value = ""
    document.getElementById("pinlet").value = ""
    document.getElementById("wta").value = ""
    document.getElementById("promo").value = ""
    document.getElementById("town").value = ""
    loadMarker(newData)
}


document.getElementById("update").onclick = upd

console.log("LPAds editor loaded!")