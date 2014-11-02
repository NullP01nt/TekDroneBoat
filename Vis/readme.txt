visualization plus how to transfer "what we want the boat to do" in to 
some data representation that is suitable for planning

Simulator:
I haven't taken Vessel (rudder steering) into account, but this is also a task that we must address - probably easier if we have data about our boat e.g. min turning radius.



Get image from google

derive data from image:
    - compute the position for each pixel:
        - global: LLH/ECEF
        - local: NED

http://developers.google.com/maps/documentation/staticmaps/?hl=da#quick_example

https://maps.googleapis.com/maps/api/staticmap?center=55.4091581,10.3815831&zoom=18&size=8000x600
http://maps.google.com/maps/api/staticmap?sensor=false&size=512x512&center=Brooklyn&zoom=12&style=feature:all|element:labels|visibility:off



I havn't taken Vessel (rudder steering) into acount, but this is also a task that we must address
