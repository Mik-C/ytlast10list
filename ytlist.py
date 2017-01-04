from bs4 import BeautifulSoup
'''
python3 -m pip install beautifulsoup4
'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getPage(youtube_user_id):
	import urllib.request
	import ssl
	url = 'https://www.youtube.com/user/%s/videos' % youtube_user_id
	context = ssl._create_unverified_context()
	page = ""
	try:
		page = urllib.request.urlopen(url, context=context).read().decode('utf-8')
	except:
		print(bcolors.FAIL + "El canal '%s' no existeix." %youtube_user_id + bcolors.ENDC)
	return page

def getVideos(youtube_user_id):
	html = getPage(youtube_user_id)
	parsed_html = BeautifulSoup(html, "html.parser")
	grid = parsed_html.find('ul', attrs={'id':'channels-browse-content-grid'})
	if grid is None:
		print()
		return
	videos = grid.find_all('div', attrs={'class':'yt-lockup-dismissable'})
	cont = 0
	for video in videos:
		if cont > 9:
			break
		print ("• %s - " %video.find('h3', attrs={'class':'yt-lockup-title'}).find('a').text +
			bcolors.BOLD + video.find('span', attrs={'class':'video-time'}).text + bcolors.ENDC)
		cont = cont + 1
	print()
	return

getVideos("Crisben93")
getVideos("ClasesAjedrez")
getVideos("Innexistent")