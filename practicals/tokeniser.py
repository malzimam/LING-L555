import sys

b = sys.stdin.read()

k=b.replace('.' , ' .')
k=k.replace(',' , ' , ')
k=k.replace('(' , ' (')
k=k.replace(')' , ' )')
k=k.replace('/', '/  ')
k=k.replace('\\', '\ ')
k=k.replace(':' , ' :')
k=k.replace('and' , ' and')
for sentencs in k.split('\n'):
	print(sentencs)
	for token in sentencs.split(' '):
		print(token, '		-	-	-	-	-	-	-	-	-	-')


