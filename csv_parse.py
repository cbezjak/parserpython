import sys
import urllib2
import csv
import time
import matplotlib.pyplot as plt
from dateutil.parser import parse

# Instanciranje praznih array-ev
x = []
y = []

# Priredi spremenljivki i vrednost 1
i = 1

# Spremenljivka url dobi iz modula argv prvi argument iz klicanja csv_parse.py skripte (torej povezavo do csv dokumenta)
url = sys.argv[1:]

# V konzolo izpisem Fetching data from: VREDNOST-PRVEGA-ARGUMENTA
print "Pridobivam podatke iz... " + url[0]

# Odprem url in v rawdata shranim kar dobim nazaj od streznika
response = urllib2.urlopen(url[0])
rawdata = response.read()
 
# V spremenljivko time shranim trenutni cas (v obliki D-M-Y)
time = (time.strftime("%d-%m-%Y"))
 
# V konzolo izpisem Shranjujem podatke
print "Shranjujem podatke"

# Spremenljivki filename priredim vrednost v obliki stringa TRENUTNI-CAS_btcdata.csv
filename = time + "_btcdata.csv"

# Shranim datoteko na disk
file_ = open(filename, 'w')
file_.write(rawdata)

# Obvezno zaprem ta file, ker ga drugace ne more uporabljati nobeni proces
file_.close()

# V konzolo izpisem Parsing  + ime datoteke
print "Parsing " + filename + "..."

# Odprem file, ki sem ga v vrstici 35 shranil 
with open(time + '_btcdata.csv', 'r') as csvfile:
	# Odprem ga z reader funkcijo iz csv knjiznice 
	plots = csv.reader(csvfile, delimiter=',')	

	next(plots, None)
	# v plots so shranjene vse vrstice v csv 
	for row in plots:
		i += 1
		y.append(float(row[1]))
		x.append(i)

# Novi plot. Ime crte na grafu je Bitcoin value 
plt.plot(x,y, label='Vrednost Bitcoina')
# Ime x osi je cas
plt.xlabel('cas')
# Ime y osi je vrednost bitcoina
plt.ylabel('vrednost bitcoina')
plt.title('Bitcoin od leta 2013')
# Naj mi graf pokaze legendo
plt.legend()
# Izrisi graf 
plt.show()