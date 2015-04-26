#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify, Response, session
import json

from PIL import Image

import urllib2 as urllib
import io

#import urllib
import cStringIO
from StringIO import StringIO
import base64

app = Flask(__name__)
app.config['DEBUG'] = True

# simple app return base64 thumbnail strings
# so html can render them on they fly

# NOTE - YOU WILL NEED TO CONFIG SHIT DEPENDING ON PLATFORM
# http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil

@app.route('/')
def index():
	return render_template( "index.html" )

@app.route('/thumbnail', methods=['GET','POST'])
def thumbmail():

	try:
		# TODO - use requests to load images from urls?

		# - opens a file. won't work for a url
		#image = Image.open( request.args['image'] )

		# - with requests
		#import requests
		#image=requests.get('http://127.0.0.1:5000/static/img/IMG_0017.JPG').content#, config={'trust_env':False}).content

		# - with url lib
		#myfile = urllib.urlopen('http://127.0.0.1:5000/static/img/hero-300x169-v2.png')
		#image = Image.open( StringIO( myfile.read()) )
		#print image.size


		myfile = urllib.urlopen(request.args['image'])
		image = Image.open( StringIO( myfile.read()) )

		if image.mode not in ("L","RGB"):
		 	image.convert("RGB")

		# print image.size[0]
		if request.args['w']:
			w = float(request.args['w'])
			#ratio=1
			if image.size[0] > w:
				ratio=image.size[0]/w

			# print 'c'
			newWidth = image.size[0]/ratio
			# print 'd'
			newHeight = image.size[1]/ratio
			# print 'e'

			#image = image.resize( [200,100], 1 )
			image.thumbnail( (newWidth,newHeight), Image.ANTIALIAS )

		img_buffer = cStringIO.StringIO()
		image.save( img_buffer, format="PNG" )	
		base_string = "data:image/png;base64,"+base64.b64encode(img_buffer.getvalue())

		print base_string

		return base_string

	except:
		print "FAILURE!"
		pass
	
	return "COMPLETE!"


# INIT APPLICATION ------------------------------------------>
if __name__=="__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(threaded=True)