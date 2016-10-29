# D={'food':'spam','quantity':4,'color':'pink'}
# print(D['food'])

# D={}
# D['food']='spam'
# D['quantity']=4
# D['color']='pink'
# print(D)
#
# rec={
#     'name':{'first':'xiangyu','last':'Wang'},
#     'job':['dev','boss'],
#     'age':18
# }
#
# print(rec['name'])
#
# rec['job'].append('coding')
# print(rec)

D = {'a':1,'b':2,'c':3}
# print(D)
#
# ks=list(D.keys())
# ks.sort()
# print(ks)
# for k in ks:
#     print(k,'=>',D[k])

# for k in sorted(D):
#     print(k,':',D[k])

## test if key exist
if 'c' in D:
    print(D['c'])

if 'e' not in D:
    print('missing')