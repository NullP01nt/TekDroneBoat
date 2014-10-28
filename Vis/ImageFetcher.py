"""
Fetching images from Google Maps over http

"""
import urllib, cStringIO
from PIL import Image, ImageFilter

#Fetch a image from google maps as a Static Map over http
class ImageFetcher: 
    size = (256,256)
    maptype="terrain" #roadmap, satellite, hybrid, terrain
    hideLabels = True

    def __init__(self, 
                lat, lon,
                zoom): #0,1,..,21
        self.lat=lat
        self.lon=lon
        self.zoom=zoom

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


#Example:
##ImageFetcher(55.4091581,10.3815831).fetch().show()

