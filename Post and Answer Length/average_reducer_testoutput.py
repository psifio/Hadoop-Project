for key in questionLengths:
    if key in answersCount:
        print key," ",questionLengths[key]
        print key," ", answersCount[key], " ", answersTotalLength[key], " ", ( (answersTotalLength[key]) / answersCount[key] )
        print "***************"
    else:
        print key," ",(questionLengths[key])
        print key," ", 0
        print "----------------"
        x=1