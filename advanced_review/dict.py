

print({x:x**2 for x in range(10)})

dic = {'k1':1,'k2':2}

for k in dic.keys():
	print(k)

for v in dic.values():
	print(v)

for item in dic.items():
	print(item)

key_view = dic.keys()
print(key_view)

dic['k3'] = 3

print(dic)