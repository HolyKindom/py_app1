M=[[1,2,3],[4,5,6],[7,8,9]]
#
# col2= [row[1] for row in M]
# print(col2)
# print M
#
# diag = [M[i][i] for i in [0,1,2]]
# print diag
#
# double = [c*2 for c in 'spam']
# print double

G=(sum(row) for row in M) #G is a iterator
print(next(G))

print(map(sum,M))