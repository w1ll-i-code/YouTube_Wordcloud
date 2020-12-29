import re
import json
import collections as col
import matplotlib.pyplot as plt


data = json.loads( open('2020.json', 'r').read() )
times = [int( re.findall('.*?T(\d\d)', a['time'])[0] ) for a in data]
distr = col.Counter(times)

plt.plot( range(0,23), [distr[key] for key in range(0,23)] )
plt.xlabel('Time')
plt.ylabel('Videos')

plt.title('Watchhistory over the day')

plt.savefig('watch_distr.png')
