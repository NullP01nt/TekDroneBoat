import math

tileSize = 256
initialResolution = 2 * math.pi * 6378137 / tileSize
# 156543.03392804062 for tileSize 256 pixels
originShift = originShift = 2 * math.pi * 6378137 / 2.0
# 20037508.342789244

def Resolution(zoom):
    return initialResolution / (2**zoom)

def LatLonToMeters( lat, lon ):
        "Converts given lat/lon in WGS84 Datum to XY in Spherical Mercator EPSG:900913"

        mx = lon * originShift / 180.0
        my = math.log( math.tan((90 + lat) * math.pi / 360.0 )) / (math.pi / 180.0)

        my = my * originShift / 180.0
        return mx, my


def MetersToPixels( mx, my, zoom):
        "Converts EPSG:900913 to pyramid pixel coordinates in given zoom level"

        res = Resolution( zoom )
        px = (mx + originShift) / res
        py = (my + originShift) / res
        return px, py


def PixelsToMeters( px, py, zoom):
    "Converts pixel coordinates in given zoom level of pyramid to EPSG:900913"

    res = Resolution(zoom)
    mx = px * res - originShift
    my = py * res - originShift
    return mx, my

def MetersToLatLon( mx, my ):
    "Converts XY point from Spherical Mercator EPSG:900913 to lat/lon in WGS84 Datum"

    lon = (mx / originShift) * 180.0
    lat = (my / originShift) * 180.0

    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180.0)) - math.pi / 2.0)
    return lat, lon
