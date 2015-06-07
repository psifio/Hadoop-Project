#!/usr/bin/python

import sys
import csv

reader=csv.reader(sys.stdin,delimiter='\t')
writer=csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)

#loop through all the posts
for line in reader:
    length=len(line)
    if length==19:
        #unpack all fields
        nodeid, title, tagnames,    author_id,    body,    node_type,    parent_id,    abs_parent_id, \
        added_at,    score,    state_string,    last_edited_id,    last_activity_by_id,    last_activity_at, \
        active_revision_id,    extra,    extra_ref_id,    extra_count,    marked = line

        #Check if post is a question and that a title line is not messed in the data        
        if author_id !="author_id" and node_type=="question":
            #split and get all tags
            tags=tagnames.split()
            for i in range(len(tags)): 
                #output key,val where key:individual tagname and val:1
                mappedLine=[tags[i], 1]
                writer.writerow(mappedLine)
    else:
    #something went wrong, continue
        continue