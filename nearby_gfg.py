import requests, json 
  
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

def nearby(query):
	#query = input('Search query: ')  
	r = requests.get(url + 'query=' + query + '&key=' + api_key)
	x = r.json()
	print(len(x['results']))
	return x['results']
	
if __name__ == '__main__':
	query = input('Search query: ')  
	y = nearby(query)
	lst = []
	for i in range(len(y)): 
		print(y[i]['name']) 
		#reference=y[i]['reference']
		if('photos' in y[i].keys()):
			photos=y[i]['photos']
			ref = photos[0]['photo_reference']
			photopr="https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="+ref+"&key="+api_key
			pic="https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key=AIzaSyBIE6dBEZAjMYKhMyN1DoIMLpGIULCH3cg"
			lst.append(photopr)
	print(lst)