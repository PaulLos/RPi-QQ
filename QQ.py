import json
import urllib
import urllib2
import hashlib
import base64
import os
import time


class QuickQuest():
	def __init__(self, folder):
		self.key = ''
		self.folder = folder
		self.read_key()
		data = self.query('start', '')
		if('n_key' in data['data']):
			self.write_key(data['data']['n_key'])
		self.read_key()
		self.download()

	def read_key(self):
		file = open(self.folder+'key.json', 'r')
		data = file.read()
		file.close()
		self.key = json.loads(data)['key']
	def query_status(self):
		pass
	def write_key(self, key):
		file = open(self.folder+'key.json', 'w+')
		file.write(json.dumps({'key': key}))
	def query(self, url, payload):
		url = 'https://api.quickquest.ru/stock/'+url
		data = json.dumps(payload)

		request = urllib2.Request(url, data)
		request.add_header('Authorization', 'Token '+self.key)
		try:
			answer = json.loads(urllib2.urlopen(request).read())
			code = 200
		except urllib2.HTTPError as e:
			code = e.code
			answer = ''
		return_array = {"data": answer, "http_code": code}
		return return_array
	def download(self):
		array = self.query('download', '')['data']
		files = os.listdir(self.folder)
		for f in files:
			if f == 'key.json':
				files.remove(f)
		files.sort()
		update = False
		for key in array:
			array[key] = base64.b64decode(array[key])
			if(key in files):
				r = self.read_file(key)
				if(r != array[key]):
					update = True
				else:
					files.remove(key)
					files.sort()
			else:
				update = True
		if len(files) != 0:
			update = True
		if update:
			self.delete_files()
			self.save_file(array)
	def write_file(self, name, data):
		f = open(self.folder+name, 'w+')
		f.write(data)
		f.close()
	def read_file(self, f):
		file = open(self.folder+f, 'r')
		data = file.read()
		file.close()
		return data
	def delete_files(self):
		files = os.listdir(self.folder)
		for f in files:
			if f != 'key.json':
				os.remove(self.folder+f)
	def save_file(self, array):
		for name in array:
			self.write_file(name, array[name])
Work = QuickQuest('/home/pi/MFRC522-python/')