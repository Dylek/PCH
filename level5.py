# level 5 http://www.pythonchallenge.com/pc/def/peak.html
import urllib.request as url
import pickle
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("PAMIĘTAJ SLowa matki")

#prounace like pickle
# pickle is module


urlString = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.loads(url.urlopen(urlString).read())
print(data)
for line in data:
    print(''.join(elmt[0] * elmt[1] for elmt in line))

# next level 6 http://www.pythonchallenge.com/pc/def/channel.html