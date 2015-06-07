import csv


reader=csv.reader(sys.stdin,delimiter='\t')

#the hash will keep key,value entries where key:nodeid of question, and value: body length
questionLengths={}
#the hash will keep the counter for a post's answers. key/value where key:nodeid, value:answers count
answersCount={}
#the hash will keep the sum  of answers' length. key/value where key:nodeid, value:answers' length
answersTotalLength={}

flagQuestion="AA"
flagAnswer="BB"

# Loop around the data
# It will be in the format: nodeid/AA or BB/ body length 
for line in reader:
    length=len(line)
    if length != 3:
        # Something has gone wrong. Skip this line.
        continue
    nodeid, flag, postLength = line
    if flag==flagQuestion:
        questionLengths[nodeid] = float(postLength)
    elif flag==flagAnswer:        
        if nodeid in answersCount:
            #nodeid encountered before -> increment counter and add length to TotalLength
            answersCount[nodeid] +=1
            answersTotalLength[nodeid] += float(postLength)
        else:
            #first appearance of a tag
            answersCount[nodeid] = 1.0
            answersTotalLength[nodeid] = float(postLength)
    else:
        pass

#iterate all node ids
for key in questionLengths:
    #if there were answers:print a)question length b) average answer length
    if key in answersCount:
        print questionLengths[key],"\t", ( answersTotalLength[key] / answersCount[key] )
    #else print a)question length b) 0		
    else:
        print questionLengths[key],"\t",0.0