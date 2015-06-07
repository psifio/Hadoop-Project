#!/usr/bin/python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter='\t')
writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)


flagQuestion="AA"
flagAnswer="BB"
#loop through all the posts
#mapped output will be
#in case of a question: node_id,"AA", len(body)
#in case of an answer: parent_id,"BB", len(body)
for line in reader:
    length=len(line)
    if length==19:
        #unpack all fields
        nodeid, title, tagnames,    author_id,    body,    node_type,    parent_id,    abs_parent_id, \
        added_at,    score,    state_string,    last_edited_id,    last_activity_by_id,    last_activity_at, \
        active_revision_id,    extra,    extra_ref_id,    extra_count,    marked = line

        #Check if a title line is messed in the data        
        if author_id =="author_id":
            continue
        #we have a post that is a question
        elif node_type=="question":
                mappedLine=[nodeid, flagQuestion, len(body)]
                writer.writerow(mappedLine)
        #we have a post that is an answer
        elif node_type=="answer":
                mappedLine=[parent_id, flagAnswer, len(body)]
                writer.writerow(mappedLine)
    else:
    #something went wrong, continue
        continue