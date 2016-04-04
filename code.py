#import from json

path = '/Users/appletree/Downloads/usagov_bitly_data2012-03-16-1331923249.txt'
import json 
records = [json.loads(line) for line in open(path)]


##read data
record[0]
record[0]['tz']

##count time zone:
from pandas import DataFrame, Series
import pandas as pd
%matplotlib inline

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()

##clean data
##replace Na, NaN
clean_tz = frame['tz'].fillna('Missing')
##replace ' '
clean_tz[clean_tz == ''] = 'Unknown'
 
##
tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
results.value_counts()[:8]


cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

print agg_counts.sum(1)
'''
tz
                                   521.0
Africa/Cairo                         3.0
Africa/Casablanca                    1.0
Africa/Ceuta                         2.0
Africa/Johannesburg                  1.0
Africa/Lusaka                        1.0
America/Anchorage                    5.0
'''

print agg_counts.sum(0)
'''
Not Windows    1194.0
Windows        2246.0
'''
