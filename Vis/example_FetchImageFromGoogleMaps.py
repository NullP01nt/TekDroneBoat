import urllib, cStringIO
from PIL import Image, ImageFilter

#URL = "https://maps.googleapis.com/maps/api/staticmap?center=55.4091581,10.3815831&zoom=18&size=8000x600"
URL = "https://maps.googleapis.com/maps/api/staticmap?center=55.4091581,10.3815831&zoom=18&size=8000x600&maptype=terrain"
file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = Image.open(file)
img.show()
