#!/usr/bin/python

import sys
import csv

oldKey=None

# Loop around the data
# It will be in the format key/value where key:author_id, value:hour_added  

#for each student i will keep the sum of posts by hour 
studentHours=[0]*24

# All the counters per hour for a particular user will be calculated,
# then we will print all the hours that are equal to the max counter

reader=csv.reader(sys.stdin,delimiter='\t')
for line in reader:
    length=len(line)
    if length != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, hour = line
    if oldKey and oldKey != thisKey:
        #find the max value of studentHours
        studentMaxhour=max(studentHours)
        #loop to print the values, this is necessary to cover multiple hours being equal to max
        for i in range(24): 
            if studentHours[i]==studentMaxhour:
                print oldKey, "\t", i
                
        oldKey = thisKey;
        #reset students array
        studentHours=[0]*24

    oldKey = thisKey
    #increment by 1, the appropriate item. E.g increment by one the posts for hour:23
    studentHours[int(hour.strip())]+=1

if oldKey != None:
    for i in range(24): 
        if studentHours[i]==studentMaxhour:
            # to print counter I could do print oldKey, "\t", i, "\t", studentHours[i]
            print oldKey, "\t", i