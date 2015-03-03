import time
import fbconsole
from fbconsole import iter_pages

fbconsole.APP_ID = '989682727717174'
targetId = '359317787470519'

fbconsole.AUTH_SCOPE = ['']
fbconsole.authenticate()

uniqueIdArray = []
count = 0;
threshhold = 100;

for post in iter_pages(fbconsole.get('/'+targetId+'/posts')):
	try:
	    for data in post['likes']['data']:
	    	id = data['id']
	    	name = data['name']
	    	if not any(id in s for s in uniqueIdArray):
	    		count+=1
	    		uniqueIdArray.append(id)
	    		print "fetched " + str(count) + " of " + str(threshhold) + " - " + name +"@"+ id
	except KeyError as e:
	    print "KeyError error({0})".format(e)
	if count >= threshhold: break

time = time.strftime("%H_%M_%S")

file = open("fbids_"+str(time)+".txt", "w")

for id in uniqueIdArray:
	file.write(id+"\n")

file.close()