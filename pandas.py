##Getting Started with pandas
##Series
obj = Series([4, 7, -5, 3])
obj.values
obj.index
##dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
##NaN
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()

obj3 + obj4

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
np.arange(5.)
## 0 1 2 3 4 
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
frame.sort_index(by=['a', 'b'])

