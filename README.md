# lpads
![title](https://raw.githubusercontent.com/crawlerop/lpads/main/lpads.png)

Many tools to work with Google Maps Location Ads.

Purpose             |  Example Command
:------------------:|:----------------------------------------------------------------------------------------------:
Parse location ads  |  python3 locadsparser.py example.json
Find ads for location | python3 locadsgetter.py 40.7127837 -74.00594130000002
Find ads for location, outputing to file | python3 locadsgetter.py 53.679895 -1.494309 -outp promos.html
Find ads for location, using proxy | python3 locadsgetter.py 40.7127837 -74.00594130000002 -proxy YOUR_PROXY_ADDRESS

## LPAds command-line arguments
Argument            |  Purpose
:------------------:|:----------------------------------------------------------:
-outp               | Change output file/folder
-noadsfail          | Fail when no ads found
-proxy              | Enabling use of proxies
-keepsearch         | Don't fail when no ads found (for Smarty Ads and Line Ads)


## Browser Support
We also ported LPAds to JavaScript! To include in your site, add in your html file:
```
<script src="https://raw.githubusercontent.com/Crawlerop/lpads/main/lpadsjs/mapads.js" crossorigin=""></script>
```
If you want the examples, please click [here](https://crawlerop.github.io/lpads/lpadsjs/mapads_marker.html)
