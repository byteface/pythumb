#PyThumb

Simple test returns base64 strings to be used for things like thumbnail images.

Basically you pass it a path to an image it will return you it resized.

Currently just pass 2 params. http path to image and a width contraint.

'''
http://localhost:5000/thumbnail
?image=http://127.0.0.1:5000/static/img/hero-300x169-v2.png
?w=100
'''

For a working example see the index.html file.

and that's almost as much as I need it for at the mo, Saves having to create/manage thumnail images on the server as I can just create them on request.

##RUN

to run the example create a virutal environment and install the requirements, then run

'''
python server.py
'''

img folder contains a mixture of PNGS and JPG files to play with but only really tested the PNGS

##NOTE
I had to use threaded=True parameter in the flask app or it would just lock up when making the image request. I think it only happens when loading images from localhost? I think that port was busy serving my app, either that or something to do with proxies? anyways I had issues with the 'requests' library and urllib and urllib2. Spent ages trying to figure out why but that resovled it. see at the bottom of the app...

'''
app.run(threaded=True)
'''