import sys

#read the file line by line,
#keep a counter for the total number of tokens
#make a matrix of word → tag
#make a separate frequency list for tags (you can use the dict datatype as described above).

pos_freq={'ADJ':0,'ADP':0,'PUNCT':0,'ADV':0,'AUX':0,'SYM':0,'INTJ':0,'CCONJ':0,'X':0,'NOUN':0,'DET':0,'PROPN':0,'NUM':0,'VERB':0,'PART':0,'PRON':0,'SCONJ':0}
ma_word={}
count_word={}
fd = open('wiki.conllu', 'r')
counter=0
for i in fd.readlines():
	i = i.strip('\n')
	if '\t' not in i:
		continue
	counter = counter+1
	row = i.split('\t')
	part=row[3]
	if part in pos_freq:
		pos_freq[part] = pos_freq[part] + 1


	if row[1] not in count_word:
		count_word[row[1]]= {}
		count_word[row[1]] = 0	
	count_word[row[1]] = count_word[row[1]] +1	

	
	if row[1] not in ma_word:
		ma_word[row[1]]= {}

	if part not in ma_word[row[1]]:
		ma_word[row[1]][part] = 0 
	ma_word[row[1]][part]=ma_word[row[1]][part]+1
print('# P','\t','count','\t','tag','\t','form')

for m in pos_freq:
	s=pos_freq[m]/counter
	print('%.2f' %s,'\t',pos_freq[m],'\t',m,'\t','_')
for t in ma_word:
	for w in ma_word[t]:
		pro= ma_word[t][w]/count_word[t]
		print('%.2f' %pro,'\t',ma_word[t][w],'\t',w,'\t',t,'\t')


fd.close()




