#!/usr/bin/env python3 

import sys
from string import Template
import datetime

replacements = {}
to_be_replaced = ['date', 
        'exercise1', 'warm_set_name1', 'warm_reps1', 'work_set_name1', 'work_reps1', 
        'exercise2', 'warm_set_name2', 'warm_reps2', 'work_set_name2', 'work_reps2',
        'exercise3', 'warm_set_name3', 'warm_reps3', 'work_set_name3', 'work_reps3',
        'exercise4', 'warm_set_name4', 'warm_reps4', 'work_set_name4', 'work_reps4',
        'exercise5', 'warm_set_name5', 'warm_reps5', 'work_set_name5', 'work_reps5',
        'exercise6', 'warm_set_name6', 'warm_reps6', 'work_set_name6', 'work_reps6',
        'exercise7', 'warm_set_name7', 'warm_reps7', 'work_set_name7', 'work_reps7',
        ]
to_replace = [datetime.datetime.now().strftime("%A, %m/%d/%Y %H:%M"), *sys.argv[1:]]
replacements = dict(zip(to_be_replaced, to_replace))

with open('template.md', 'r') as f:
    temp = f.read()

out_journal = Template(temp).substitute(replacements)

with open('training_journal.md', 'r+') as outf:
    content = outf.read()
    outf.seek(0, 0)
    outf.write(out_journal + content)
