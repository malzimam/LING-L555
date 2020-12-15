# Program to count relative frequencies of pro-drop vs. non-prodrop subjects in arabic verbs by aspect
# Assumptions:
# - If a verb does not have a subject dependent then it is pro-drop
import sys
fd = open('ar_padt-ud-dev.conllu', 'r')
# subjects of verbs e.g. subjects[(3, 4)] = 1
subjects={}
# verbs and their aspect, e.g. verbs[(3, 4)] = 'Imp'
verbs= {}
sent_id = 1 # we need to be able to distinguish between the different sentences
# read in each of the lines from the conllu file
for i in fd.readlines():
    i = i.strip('\n')
    if i =='':
        sent_id += 1 # incremenet the sentence ID by one 
    if '\t' not in i:
        continue
    row = i.split('\t')
    if '-' in row[0] or '.' in row[0]:
        continue
    part=row[3] # this is the part of speech
    idx= int(row[0]) # This is the index, we convert the string to an integer using int() in case we need to compare the indexes
    deprel = row[7]
    head = int(row[6])
    feats = row[5]
    # if the part of speech is in the verb dictionary then add the index to the verb list
    if part == 'VERB':
        if 'Aspect=Imp' in feats:
            verbs[(sent_id, idx)] = 'Imp'
        elif 'Aspect=Perf' in feats:
            verbs[(sent_id, idx)] = 'Perf'
        else:
            verbs[(sent_id, idx)] = '???'
    # if the deprel of the token is 'nsubj' (e.g. in the nsubj1 dictionary)
    if deprel == 'nsubj':
        # in the nsubj2 dictionary, add a lookup of index -> head
        subjects[(sent_id, head)]= idx
# Then you iterate over verbs.items()
# and count up the ones that have Perf in verbs and no subject
imp_no_subj = 0
perf_no_subj = 0
imp_with_subj = 0
perf_with_subj = 0
for (sid, idx) in verbs.keys():
    if verbs[(sid, idx)] == 'Imp':
        if (sid, idx) in subjects:
           imp_with_subj += 1
        else:
            imp_no_subj += 1
    if verbs[(sid, idx)] == 'Perf':
        if (sid, idx) in subjects:
            perf_with_subj += 1
        else:
            perf_no_subj += 1

print('The number of null subject given to imperfect aspect:',imp_no_subj)
print('The number of subject given to imperfect aspect:',imp_with_subj)

print('The portion of null subject given to Imperfect aspect:',"{0:.0f}%".format(imp_no_subj/(imp_with_subj+imp_no_subj)*100))
print('The portion of subject given to Imperfect aspect:',"{0:.0f}%".format(imp_with_subj/(imp_with_subj+imp_no_subj)*100))

print('The number of null subject given to perfect aspect:',perf_no_subj)
print('The number of subject given to perfect aspect:',perf_with_subj)

print('The portion of non-null subject given to perfect aspect:',"{0:.0f}%".format(perf_no_subj/(perf_with_subj+perf_no_subj)*100))
print('The portion of subject given to perfect aspect:',"{0:.0f}%".format(perf_with_subj/(perf_with_subj+perf_no_subj)*100))
fd.close()
