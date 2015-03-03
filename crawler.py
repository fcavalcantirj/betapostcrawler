import time
import fbconsole
import calendar
import datetime
from fbconsole import iter_pages

def add_months(sourcedate,months):
	month = sourcedate.month - 1 + months
	year = sourcedate.year + month / 12
	month = month % 12 + 1
	day = min(sourcedate.day,calendar.monthrange(year,month)[1])
	return datetime.date(year,month,day)

#beta_posts_crawler
fbconsole.APP_ID = '989682727717174'

#MEU RIO
#targetId = '241897672509479'

#WazeBr
targetId = '359317787470519'

fbconsole.AUTH_SCOPE = ['']
fbconsole.authenticate()

uniqueIdArray = []
count = 0;
threshold = 50000;

initialDate = datetime.datetime.strptime('2011-01-01', '%Y-%m-%d').date()
until = datetime.datetime.strptime('2011-12-01', '%Y-%m-%d').date()

while count < threshold:
	print "from=["+str(initialDate)+"].until=["+str(until)+"]"
	for post in iter_pages(fbconsole.get('/'+targetId+'/posts?since='+initialDate.strftime("%Y-%m-%d")+'&until='+until.strftime("%Y-%m-%d")+'&limit=250')):
		try:
		    for data in post['likes']['data']:
		    	id = data['id']
		    	name = data['name']
		    	if not any(id in s for s in uniqueIdArray):
		    		count+=1
		    		uniqueIdArray.append(id)
		    		print "fetched " + str(count) + " of " + str(threshold) + " - " + name +"@"+ id
		except KeyError as e:
		    print "KeyError error({0})".format(e)
		except fbconsole.OAuthException as o:
			print "OAuthException ({0})".format(o)
			fbconsole.authenticate()
	initialDate = until
	until = add_months(until,1)
	if until >= datetime.datetime.now().date():
		break

time = time.strftime("%H_%M_%S")

file = open("fbids_"+targetId+"_"+str(time)+".txt", "w")

for id in uniqueIdArray:
	file.write(id+"\n")

file.close()