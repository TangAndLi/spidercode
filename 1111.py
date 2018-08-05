# def testFun():
# 	temp = [lambda x:i*x for i in range(4)]
# 	return temp
#
# for everyLambda in testFun():
# 	print (everyLambda(2))

# [lambda x : i*x, lambda x : i*x, lambda x : i*x,lambda x : i*x]
# # [1,1,1,1]
def fn1():
    fn = [lambda x:i+x for i in range(4)]
    return fn

for i in fn1():
    print(i(1))

def fn2(x):
    def fn3(y):
        return x + y
    return fn3
fn3 = fn2(3)
print(fn3(3))

# list2 = ['a''b''c']
# list1 = 'a' 'b' 'c' 'd'
# print(list2)
# print(list1)
# print(type(list1))

# fn = lambda x,y:x+y
# print(fn(1,2))






