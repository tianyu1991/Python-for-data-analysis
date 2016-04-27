
##read data
#import from json
path = '/Users/appletree/Downloads/usagov_bitly_data2012-03-16-1331923249.txt'
import json 
records = [json.loads(line) for line in open(path)]
##import from table
users = pd.read_table('ml-1m/users.dat', sep='::', header=None,
names=unames)
names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])

##data frame
record[0]['tz']
users[:5]

##count time zone:
from pandas import DataFrame, Series
import pandas as pd


frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()

##clean data
##replace Na, NaN
clean_tz = frame['tz'].fillna('Missing')
##replace ' '
clean_tz[clean_tz == ''] = 'Unknown'
cframe = frame[frame.a.notnull()]
 
##
tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
results.value_counts()[:8]





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
indexer = agg_counts.sum(1).argsort()
##numpy.argsort(a, axis=-1, kind='quicksort', order=None)
##kind : {‘quicksort’, ‘mergesort’, ‘heapsort’}, optional
##return a array of indices that sort a along the specified axis. In other words, a[index_array] yields a sorted a.

count_subset = agg_counts.take(indexer)[-10:]
count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
##normalize

##concate
NewDataFrame=pd.concat([DataFrame, DataFrame2]) ##concate by row
NewDataFrame=pd.concat([DataFrame, DataFrame2], axis=1) ##concate by col

##merge
NewDataFrame=DataFrameLeft.merge(DataFrameRight, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False)
NewDataFrame=pd.merge(DataFrameLeft, DataFrameRight, ...)
##how : {‘left’, ‘right’, ‘outer’, ‘inner’},
##If on is None and not merging on indexes, then it merges on the intersection of the columns by default.

##group_by
group_name = np.where(DataFrame['colname1'].str.contains('groupA'),'groupA', 'groupB')
##group by if colname1 contain word "groupA"
NewDataFrame = DataFrame.groupby(['colname2', group_name])
##                   groupA      groupB
##colname2_group1      4           4
##colname2_group2      5           6
##...

NewDataFrame = DataFrame.groupby('colname2').size()
##one group, count number of each group
##colname2_group1      8
##colname2_group2      11

##pivot
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
##sort
NewDataFrame= DataFrame.sort_index(by='col', ascending=False)
##reverse sort
NewDataFrame[::-1]
 

##plot
%matplotlib inline
DataFrame.plot(kind='barh', rot=0)
table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female',
 legend=False)


'Hello, %s' % 'world'
##'Hello, world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)
##'Hi, Michael, you have $1000000.'
'%.2f' % 3.1415926
##'3.14'
##%d	int
##%f	float
##%s	str
##%x	int(16)
