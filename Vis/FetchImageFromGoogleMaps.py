import urllib, cStringIO
from PIL import Image, ImageFilter

#Fetch a image from google maps as a Static Map over http
class ImageFetcher:
    lat=55.3738577
    lon=10.3983709
    zoom=18 #0,1,..,21
    size = (800,600)
    maptype="terrain" #roadmap, satellite, hybrid, terrain
    hideLabels = True

    def __init__(self, lat, lon):
        self.lat=lat
        self.lon=lon

    def getURL(self):
        url = "http://maps.googleapis.com/maps/api/staticmap?"
        url+="center="+str(self.lat)+","+str(self.lon)
        url+="&zoom="+str(self.zoom)
        url+="&size="+str(self.size[0])+"x"+str(self.size[1])
        url+="&maptype="+self.maptype
        if(self.hideLabels):
            url+="&style=feature:all|element:labels|visibility:off"
        return url        
    
    def fetch(self):
        file = cStringIO.StringIO(urllib.urlopen(self.getURL()).read())
        return Image.open(file)

ImageFetcher(55.4091581,10.3815831).fetch().show()


