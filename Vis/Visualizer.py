import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import ImageFetcher
import Conversion
zoom=16


class Drone:
    __handleRadius = 10
    __circle = None

    def __init__(self, initialPosition, initialOrientation):
        self.__setPosition(initialPosition) 
        self.__orientation = initialOrientation 
        print self  
    
    def __str__(self):
        return "drone: position="+str(self.__position)+" orientation="+str(self.__orientation)

    def __setPosition(self, newPosition):
        self.__position = newPosition
        if self.__circle is not None:
            self.__circle.center = newPosition

    #Drone drawing
    def setupDrawing(self, figure):
        centerX, centerY = self.__position[0],self.__position[1]
        self.__circle = plt.Circle((centerX,centerY), self.__handleRadius,fc=np.random.random(3),picker=True, alpha=0.5)
        figure.gca().add_patch(self.__circle)
        
    def move(self, newPosition, index):
        print "moving a Drone"
        if newPosition is not None:
            self.__setPosition(newPosition)

class Path:
    __handleRadius = 6
    __controlPoints={}
    __controlPointsCircles={}
    __controlPointsLines=None
    __curves=None

    def move(self, position, index):
        if index is not None:
             self.__setControlPoint(index, position)


    def __init__(self, viaPoints):
        for (i,p) in zip(range(0,len(viaPoints)),viaPoints):   
            self.__setControlPoint(i, p)

    #map from matplotlib-artists to some object that can change data
    __artistToControlPointIndex={}


    def __setControlPoint(self, index, coordinates):
        #Set control point with the give index (start at zero)
        global __controlPoints
        self.__controlPoints[index] = coordinates
        if index in self.__controlPointsCircles.keys():
            self.__controlPointsCircles[index].center = coordinates            

        #connecting lines
        if self.__controlPointsLines is not None:
            xy = self.getXYCoordinatList()
            self.__controlPointsLines[0].set_xdata(xy[0])
            self.__controlPointsLines[0].set_ydata(xy[1])

        #update the quartic polynomials ...

        #and connecting curves...

    def getControlPointsDict(self):
        return (self.__controlPoints)

    def getXYCoordinatList(self):
        xList = []
        yList = []
        for p in self.__controlPoints.values():
            xList.append(p[0])
            yList.append(p[1])
        return (xList, yList)

    #Path drawing
    def setupDrawing(self, figure):
        #connecting lines
        xy = self.getXYCoordinatList()
        self.__controlPointsLines = figure.gca().plot(xy[0], xy[1])

        #Prepare for picking events
        for i,p in self.__controlPoints.iteritems():
            centerX, centerY = p[0], p[1]
            circle = plt.Circle((centerX,centerY), self.__handleRadius,fc=np.random.random(3),picker=True, alpha=0.5)
            self.__controlPointsCircles[i]=circle
            figure.gca().add_patch(circle)

            #Prepare for picking events
            self.__artistToControlPointIndex[circle]=i

    #Picking logic for Path control points
    def selectControlPoint(self, artist):
        if(artist in self.__artistToControlPointIndex):
            controlIndex = self.__artistToControlPointIndex[artist]
            return(controlIndex)

################################################################################


#Plot
plt.ion()
figure = plt.figure('map')
figure.gca().set_aspect('equal')


#make a Catmull Rom spline path
path = Path([np.array([ 84, 200]),
             np.array([ 67,  88]),
             np.array([165,  22]),
                 np.array([230,  160])])
path.setupDrawing(figure)


#make the drone
drone = Drone(np.array([ 31, 165]), 0)
drone.setupDrawing(figure)

#State for user picking logic 
movable = None
index = None #spline path controle point index

def on_pick(event):
    global movable,index
    index = path.selectControlPoint(event.artist)
    if index is not None:
        movable = path
    else:
        movable = drone

def motion_notify_event(event):
    global figure
    if movable is not None:
        movable.move(np.array([event.xdata, event.ydata]), index)
    figure.canvas.draw()

def button_press_event(event):
    pass

def button_release_event(event):
    global movable, index
    movable, index = None, None

figure.canvas.mpl_connect('pick_event', on_pick)
figure.canvas.mpl_connect('motion_notify_event', motion_notify_event)
figure.canvas.mpl_connect('button_press_event', button_press_event)
figure.canvas.mpl_connect('button_release_event', button_release_event)

#Background image
image = ImageFetcher.ImageFetcher(55.410600, 10.379845, zoom).fetch()	
plt.imshow(image)

#Disable default keys on the plot e.g. 'k' is logaritmic scale
figure.canvas.mpl_disconnect(figure.canvas.manager.key_press_handler_id)

#Display the figures on screen
plt.show(block=True)

################################################################################

def printCoordinates(event):
    global figure
    if event.xdata is not None and event.ydata is not None:
        px, py = np.ceil(event.xdata), np.ceil(event.ydata)
        print("pixel: "+str(px)+", "+str(py))
        mx, my=Conversion.PixelsToMeters(px, py, zoom)
        print("mx="+str(mx)+" my="+str(my))
        lat, lon=Conversion.MetersToLatLon( mx, my )
        print("Lat="+str(lat)+" lon="+str(lon) +"    "+ str(lat)+","+str(lon))


