#!/usr/bin/python
import sys
import csv

reader=csv.reader(sys.stdin,delimiter='\t')
writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

#loop through all the posts
#mapped output will be
#a)in case of a question: node_id, author_id
#b) in case of an answer or a comment: parent_id, author_id
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
                mappedLine=[nodeid, author_id]
                writer.writerow(mappedLine)
        #we have a post that is an answer or a comment
        elif node_type=="answer":
                mappedLine=[parent_id, author_id]
                writer.writerow(mappedLine)
        elif node_type=="comment":
                mappedLine=[abs_parent_id, author_id]
                writer.writerow(mappedLine)				
    else:
    #something went wrong, continue
        continue