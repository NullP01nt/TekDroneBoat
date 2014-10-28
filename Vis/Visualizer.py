import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import ImageFetcher
import Conversion

zoom=0

def motion_notify_event(event):
    global figure
    if event.xdata is not None and event.ydata is not None:
        px, py = np.ceil(event.xdata), np.ceil(event.ydata)
        print("pixel: "+str(px)+", "+str(py))
        mx, my=Conversion.PixelsToMeters(px, py, zoom)
        print("mx="+str(mx)+" my="+str(my))
        lat, lon=Conversion.MetersToLatLon( mx, my )
        print("Lat="+str(lat)+" lon="+str(lon) +"    "+ str(lat)+","+str(lon))
        print

#Plot
plt.ion()
figure = plt.figure('map')
#figure.gca().set_aspect('equal')
figure.canvas.mpl_connect('motion_notify_event', motion_notify_event)

image = ImageFetcher.ImageFetcher(0,0, zoom).fetch()	#55.409600, 10.379845
plt.imshow(image)
plt.show(block=True)

