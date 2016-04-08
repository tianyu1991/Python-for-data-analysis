##Getting Started with pandas
##Series
obj = Series([4, 7, -5, 3])
obj.values
obj.index
##dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj = Series(sdata)
##NaN
pd.isnull(obj)
pd.notnull(obj)
obj.isnull()
data.dropna(axis=1, how='all')  ##only drop cols that are all NA:
df.fillna(0, inplace=True)##fillna returns a new object by default, but you can modify the existing object in place
df.fillna(method='ffill', limit=2)

##create data frame
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
##       year  state  pop  debt 
## one
## two
## three
## four 
## five
frame2.ix['three']
frame2['debt']
data.ix['three', ['debt', 'state']]
data.ix[data.ebt > 5, :3]
##Index objects are immutable and thus can’t be modified by the user:
frame2.reindex(['a', 'b', 'c', 'd', 'e'])
frame.reindex(columns=['...','...',...])

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')
'''
0 blue
1 blue
2 purple
3 purple
4 yellow
5 yellow
'''
##ffill or pad Fill (or carry) values forward
##bfill or backfill Fill (or carry) values backward

df1+df2      #results in NA values in the locations that don’t overlap:
df1.add(df2, fill_value=0)  ##

arr = np.arange(12.).reshape((3, 4))
#array([[ 0., 1., 2., 3.],
#       [ 4., 5., 6., 7.],
#       [ 8., 9., 10., 11.]])
arr - arr[0]
#array([[ 0., 0., 0., 0.],
#       [ 4., 4., 4., 4.],
#       [ 8., 8., 8., 8.]])

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde')) ##use string list['b','d','e'] to name columns
frame.sub(frame['b'], axis=0)

data.drop([index1,index2])
data.drop(col,axis=1)

###     1    2    3
### A
### B
### C

frame.apply(f)
##  1
##  2
##  3

frame.apply(f,axis=1)
## A
## B
## C

'%.2f' % x

##sort
frame.sort_index(by=['a', 'b']) ## a,b are col names,sort by multiple columns
frame.sort_index(axis=1,ascending=False)
obj.rank(method-'')
#'average' Default: assign the average rank to each entry in the equal group.
#'min' Use the minimum rank for the whole group.
#'max' Use the maximum rank for the whole group.
#'first' Assign ranks in the order the values appear in the data.

df.mean(axis=1, skipna=False)
df.describe()##Compute set of summary statistics for Series or each DataFrame column
count()#Number of non-NA values
#sum() ,mean(),median(), var(),std(),skew(),kurt(),cumsum(),cumprod,cummin, cummax,diff,pct_change, Compute percent changes
frame.corr()
frame.cov()
frame1.corrwith(frame2.col1)


data.unstack()
data.stack()

##hierarchical index
frame = DataFrame(np.arange(12).reshape((4, 3)),
       index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
       columns=[['Ohio', 'Ohio', 'Colorado'],
       ['Green', 'Red', 'Green']])
frame2 = frame.set_index(['c', 'd'], drop=False)##use col c, d as hierarchical index, By default the columns are removed from the DataFrame
frame2.reset_index()  ## the hierarchical index move back to col
       
data.drop_duplicates()
data.replace({-999: np.nan, -1000: 0})##dict
data.replace([-999, -1000], [np.nan, 0])
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})

###Discretization and Binning
pd.cut(ages, [18, 26, 36, 61, 100], labels=['Youth', 'YoungAdult', 'MiddleAged', 'Senior'],right=False)
data = np.random.rand(20)
pd.cut(data, 4, precision=2)##a integer number of bins instead of explicit bin edges
pd.qcut(data, 4) # Cut into quartiles
