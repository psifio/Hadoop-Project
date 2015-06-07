#!/usr/bin/python

import sys
import csv


reader=csv.reader(sys.stdin,delimiter='\t')

#the hash will keep key,value entries where key:tagName, and value:Counter for this tag
h={}

# Loop around the data
# It will be in the format key/value where key:tagName, value: constant alvays equal to 1 
for line in reader:
    length=len(line)
    if length != 2:
        # Something has gone wrong. Skip this line.
        continue
    tagName = line[0]
    if tagName in h:
        #increment tag counter
        h[tagName]+=1
    else:
        #first appearance of a tag
        h[tagName]=long(1)

#sort the tag names according to their counter values
sortedTags= sorted(h,key=h.get,reverse=True)


#we want to cover the possibility of having tags with equal occurrence
#e.g the top tag could have 250 occurrences, but the second,third, e.t.c 100 occurrences
#so we print tagNames till a)either we have 10 different counter values, OR b)we  run out of tags
i=long(0)
length=len(sortedTags)
valueChanged=0
lastValue=0
#by changing this value we can get top 0, top 3 e.t.c values
topLimit=10
while i<length and valueChanged<=topLimit:
    currentTag=sortedTags[i]
    if (lastValue!=h[currentTag]) :
        valueChanged+=1
        lastValue=h[currentTag]
    if valueChanged<=topLimit:
        print currentTag,"\t", h[currentTag]
    i+=1