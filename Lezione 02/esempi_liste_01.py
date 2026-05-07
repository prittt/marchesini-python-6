l = [1, 2, 3]
t = (1, 2, 3)

l2 = list(t)

for i in range(len(l)):
    print(l[i])

for e in l:
    print(e)

for i, e in enumerate(l):
    print(i, e)


#l[len(l)]
l[-1]

l_copy = l[:10]
#l_copy = l[::-1]
print(l_copy)

def foo():
    return 1, 2, 3

ret = foo()
print(ret)
print(type(ret))

a, b, _ = foo()
#print(a, b, type(a), type(b))

