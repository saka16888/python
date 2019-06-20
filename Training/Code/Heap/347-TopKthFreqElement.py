import collections, heapq

data = [1,5,3,2,8,5]
print("before heapify, data =",data)
heapq.heapify(data)
print("after heapify, heap sort, data =",data)
# for i in range(len(data)):
#     print("pop =" ,heapq.heappop(d1)) # print 1

print("----------- heap sort ----------------------" )
data = [1,5,3,2,8,5]
d1=heapq.heapify(data)
heapq.heapreplace(data,10) #  删除现有最小元素并替换成新值
print("d1 =",d1)

print("pop =" ,heapq.heappop(data))
print("pop =" ,heapq.heappop(data))
print("push pop =" ,heapq.heappushpop(data,6))

print("---------------------------------" )
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue','green']:
    cnt[word] += 1
print("cnt =",cnt)

print("---------------------------------" )
num_count=collections.Counter(cnt)
print("num_count = ",num_count)
k=2
keys=heapq.nlargest(k,num_count)
print(keys)

for key in keys:
    print(key,'=',num_count[key])

print("---------------------------------" )
print("-" * 60)
coll=collections.Counter()
input_list=[1,3,5,1,'a',56,'b','b','d','3']
for i in input_list:
    coll[i] += 1
print(coll)

print("---------------------------------" )

data = [1,5,3,2,8,5]
print(heapq.nlargest(3, data))
print(heapq.nsmallest(3, data))

print("---------------------------------" )
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print("cheap = ",cheap," expensive =",expensive)
