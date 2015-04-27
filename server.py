#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template#, jsonify, Response, session
#import json

from PIL import Image

import urllib2 as urllib
#import urllib
#import io
import cStringIO
from StringIO import StringIO
import base64

app = Flask(__name__)
app.config['DEBUG'] = True


# router ----

@app.route('/')
def index():
	return render_template( "index.html" )


@app.route('/list')
def list():
	"""
	test rendering a list in a flask template
	"""
	somelist=[ { 'link':'http://127.0.0.1:5000/static/img/landscape.png' },\
	{ 'link':'http://127.0.0.1:5000/static/img/portrait.JPG' },\
	{ 'link':'http://127.0.0.1:5000/static/img/square.png' },\
	{ 'link':'http://127.0.0.1:5000/static/img/test.png' },\
	{ 'link':'http://127.0.0.1:5000/static/img/transparent.png' }]

	return render_template( "list.html", list=somelist )


@app.route('/thumbnail', methods=['GET','POST'])
def thumbnail():
	return generate_thumbnail( request.args['image'], float( request.args['w'] ) );



# functions ----

def generate_thumbnail( url, width ):
	"""
	url - a http url
	width - cast as float if grabbing off a request arg
	"""
	try:

		# - opens a file. won't work for a url.
		# this need to be a path to a file not http then uncomment the urllib stuff
		#image = Image.open( request.args['image'] )

		# - with requests
		#import requests
		#image=requests.get('http://127.0.0.1:5000/static/img/IMG_0017.JPG').content#, config={'trust_env':False}).content

		# - with url lib
		#myfile = urllib.urlopen('http://127.0.0.1:5000/static/img/hero-300x169-v2.png')
		#image = Image.open( StringIO( myfile.read()) )
		#print image.size


		myfile = urllib.urlopen(url)
		image = Image.open( StringIO( myfile.read()) )


		if image.mode not in ("L","RGB"):
		 	image.convert("RGB")


		if width:
			w = float(width)
			#ratio=1
			if image.size[0] > w:
				ratio=image.size[0]/w

				newWidth = image.size[0]/ratio
				newHeight = image.size[1]/ratio

				#image = image.resize( [200,100], 1 )
				image.thumbnail( (newWidth,newHeight), Image.ANTIALIAS )


		img_buffer = cStringIO.StringIO()
		image.save( img_buffer, format="PNG" )	
		base_string = "data:image/png;base64,"+base64.b64encode(img_buffer.getvalue())

		#print base_string
		return base_string

	except:
		print "FAIL!"
		pass
	
	return "FAIL!"



# context processor to make function available in templates
@app.context_processor
def thumbnail_processor():
	def getThumbnail( path, width ):
		return generate_thumbnail( path, width )
	return dict(getThumbnail=getThumbnail)



# INIT APPLICATION ----
if __name__=="__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(threaded=True)