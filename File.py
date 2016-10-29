#coding=UTF-8

# f=open('data.txt','w')
# f.write('hello\n')
# f.write('world\n')
# f.close()

f=open('data.txt')
text=f.read()
print(text)

print(text.split())

Y={'a','b','c'}#set是无序集合
X=set('spam')#集合可以通过set函数创建 目标对象不可变
print(Y)
print(X)
print(X&Y)
print(X|Y)