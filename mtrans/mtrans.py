import json,urllib
class Google:
	def __init__(self,API):
		self.API=API
		self.url="https://www.googleapis.com/language/translate/v2"

	def translate(self,translate,from_lang,to_lang):
		response=self.url+"?key={0}&q={1}&source={2}&target={3}".format(self.API,translate.replace(' ','%20'),from_lang,to_lang)
		return json.loads(urllib.urlopen(response).read())

	def detect(self,translate):
		response=self.url+str("/detect?key={0}&q={1}").format(self.API,translate.replace(' ','+'))
		return json.loads(urllib.urlopen(response).read())
