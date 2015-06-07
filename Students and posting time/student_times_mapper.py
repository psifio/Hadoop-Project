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

        #just a check that title line is not in the data        
        if author_id !="author_id":
            #calculate hour from added_at
            hour=added_at[11:13]
            #output key, val where key:author_id and val:hour
            mappedLine=[author_id, hour]
            writer.writerow(mappedLine)
    else:
    #something went wrong, continue
        continue