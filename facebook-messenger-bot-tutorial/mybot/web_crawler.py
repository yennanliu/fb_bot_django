from bs4 import BeautifulSoup
import requests, re
import pandas as pd 
import urllib 
import random



# Chat 
# ipeen 
# Carousell 
# ptt 
# airbnb
# movie / music 


# ====================================================

def regular_chat():
	sample_response = ['HI THERE', 'WAZZA UP','R U KIDDING ME', '..?']
	response = sample_response[random.randint(0,3)]
	print (response)
	return response

# ====================================================

# Carousell


def Caro_grab_(query):
	url = 'https://tw.carousell.com/search/products/?query={}'
	url=url.format(query)
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	anchors = soup.find_all('a', {'class': 'pdt-card-thumbnail', 'href': True})
	content='' 
	url_refix = 'https://tw.carousell.com/p/'
	for anchor in anchors:
		for k in re.findall('\d+', anchor['href']):
			if len(k) > 3:
				url = url_refix + k 
				content += anchor.find('img')['alt'] + "\n" + str(url) + "\n\n"

	print (content)
	return content[:600]


def Caro_grab():
	url = 'https://tw.carousell.com/?hl=en'
	opener=urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page,"html.parser")
	anchors = soup.find_all('a', {'class': 'pdt-card-thumbnail', 'href': True})
	content='' 
	url_refix = 'https://tw.carousell.com/p/'
	for anchor in anchors:
		for k in re.findall('\d+', anchor['href']):
			if len(k) > 3:
				#print (anchor.find('img')['alt'])
				#print (url_refix + k)
				url = url_refix + k 
				#print (url)
				#print ('\n')
				content += anchor.find('img')['alt'] + "\n" + str(url) + "\n\n"

	print (content)
	return content[:600]





# ====================================================

### ipeen


def ipeen_grab():
	output = [[] for k in range(2)]
	for page in range(1,5):
	    url ='http://www.ipeen.com.tw/search/all/000/0-100-0-0/%E4%B8%AD%E5%BC%8F/?p={}&adkw=%E5%8F%B0%E5%8C%97'.format(page)
	    print (url)
	    opener=urllib.request.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    page = opener.open(url)
	    soup = BeautifulSoup(page)
	    for k in soup.find_all('a', attrs={'data-label': '店名'}):
	        output[0].append(k.text)

	    for k in soup.findAll('span',{"style":"padding-left:3em;"}):
	        output[1].append(k.get_text())
	data = ''
	for k, m in zip(output[0],output[1]):
	    data += str(k) + str(m)
	# limit number of query response here, since there may be limit in msg length 
	return data[:600]


# ==================================================== 

### ptt beauty 


def ptt_beauty():
	url = 'https://www.ptt.cc/bbs/Beauty/index.html'
	rs = requests.session()
	res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html', verify=False)
	soup = BeautifulSoup(res.text, 'html.parser')
	#ALLpageURL = soup.select('.btn.wide')[1]['href']
	content=''
	# limit number of query response here, since there may be limit in msg length 
	for k in soup.find_all('a',href=True)[:15]:
    #if 'Beauty' in k['href']:
	    try:
	    	if len(k['href']) < 30:
	    		pass
	    	else:
	            print ("https://www.ptt.cc/"+ k['href'], k.text)
	            content +=  k.text + "\n" + 'https://www.ptt.cc%s'%(k['href']) + "\n\n"
	            #content += 'Beauty/M.1423752558.A.849.html' + "\n\n" #+ 'https://www.ptt.cc/'+ k['href'] + "\n\n" 
	            #content += k.text + "\n\n"
	            #content = "https://www.ptt.cc/bbs/Beauty/M.1491126397.A.79A.html"
	    except:
	        pass
	#content = []
	#content = "this is content \n 123 \n 456 "
	print ('==================')
	print (content)
	return content



# ====================================================

#if __name__ == "__main__":
#	pass
	#Caro_grab()
	#regular_chat()
	#ptt_beauty()
	#pttBeauty()






