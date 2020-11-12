import sys


trans_lsit ={}


fd = open('trans.txt', 'r')
for i in fd.readlines():
	i = i.strip('\n')
	if '\t' not in i:
        	continue
	row = i.split('\t')
	if len(row) != 2:
        	continue
	trans_lsit[row[0]]= row[1]

	
fd.close() 
#print(trans_lsit)


for line in sys.stdin.readlines(): 
	if '\t' not in line:
		print(line.strip())
		continue
	row = line.split('\t')
	#print(row)
	
	form = row[1]
	for item in form:
		if item not in trans_lsit:
			continue
		form=form.replace(item, trans_lsit[item])

	print(row[0],'\t',row[1],'\t_\t_\t_\t_\t_\t_\t_','IPA='+form,)



