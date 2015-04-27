#PyThumb

Pass in images urls, returns base64 strings. use for things like thumbnails

Currently just pass 2 params. http path to image and a width constraint. i.e.
```
http://localhost:5000/thumbnail?image=http://127.0.0.1:5000/static/img/landscape.png?w=100
```
will return something like...
```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAABLCAIAAACwbjOoAAAd4UlEQVR4nE16Waxm2XXWt9ba+0z/f+d...
```

For a working example run the app and also check out the code in...
server.py
index.html

that's as much as I need it for at the mo, Saves having to create/manage thumbnail images on the server as I can just create them on request.

##RUN
to run the example create a virutal environment and install the requirements, then run
```
python server.py
```

##lists
if you like Flask checkout the list renderer http://localhost:5000/list

and the list.html template for implementation


img folder contains a mixture of PNGS and JPG files to play with


##NOTE
I had to use threaded=True parameter in the flask app or it would just lock up when making the image request. I think it only happens when loading images from localhost? I think that port was busy serving my app, either that or something to do with proxies? anyways I had issues with the 'requests' library and urllib and urllib2. Spent ages trying to figure out why but that resovled it. see at the bottom of the app...
```
app.run(threaded=True)
```

##YOU WILL NEED TO CONFIG STUFF DEPENDING ON PLATFORM
http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil

