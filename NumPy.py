#NumPy
data = [[1, 2, 3, 4], [5, 6, 7, 8],dtype=int64]
##int8,int16,int32,int64,float16,...float128,complex64,128,256,bool,object,string_,unicode_
arr = np.array(data)
arr.ndim
#2
arr.shape
#(2,4)
arr.dtype
#dtype('int64')
np.zeros((3, 6))
#array([[ 0., 0., 0., 0., 0., 0.],
#[ 0., 0., 0., 0., 0., 0.],
#[ 0., 0., 0., 0., 0., 0.]])
np.ones()
np.empty()
np.eye()
#Create a square N x N identity matrix
float_arr = arr.astype(np.float64)
arr * arr
arr - arr
1 / arr
arr ** 0.5
##^0.5
arr = np.arange(10)
np.arange(-5, 5, 0.01)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
##An important first distinction
##from lists is that array slices are views on the original array. This means that
##the data is not copied, and any modifications to the view will be reflected in the source
##array,copy, arr2 = arr.copy()

arr[0][2]
arr[0,2]
arr.T   #Transposing
np.exp()
sign() #Compute the sign of each element:
sqrt,square,log,modf  ##Return fractional and integral parts of array as separate array
isnan,isfinite, isinf
randn(8)
np.random.normal(size=(4, 4))
##rand(a uniform distribution), randint,binomial,uniform
np.maximum(x, y)
##std, var,mean,sum
bools.any()  ##if any true
bools.all()  ## if all true
arr.sort()
unique(x)
intersect1d(x, y)
union1d(x, y)
np.save('some_array', arr)   ##save into some_array.npy
np.load('some_array.npy')
np.savez('array_archive.npz', a=arr, b=arr)  ##save multiple arrays
np.loadtxt('array_ex.txt', delimiter=',')
x.dot(y)  ##Matrix multiplication

np.where(pd.isnull(a), b, a) ## a==nan, then b. else: a
