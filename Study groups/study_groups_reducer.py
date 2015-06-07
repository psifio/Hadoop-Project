#!/usr/bin/python
import sys
import csv

oldKey = None


#in the list we will add all the users that participated in the current thread (thisKey)
threadusersList = []


#will print without quotes
#writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
writer=csv.writer(sys.stdout,delimiter='\t')

reader=csv.reader(sys.stdin,delimiter='\t')
# Loop around the data
#It will be in the format thread_id\author_id
#For each line add the author_id in the hash 
for line in reader:
     if len(line) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisAuthorId = line
    if oldKey and oldKey != thisKey:
        #maybe we should check: 'if len(threadusersList)>1' to avoid printing orphan questions, 
        #however the exercise does not mention so
        threadusersList.sort()
        writer.writerow(threadusersList)

        oldKey = thisKey;
        threadusersList = []

    oldKey = thisKey
    threadusersList.append(thisAuthorId)

if oldKey != None:
    threadusersList.sort()
    writer.writerow(threadusersList)