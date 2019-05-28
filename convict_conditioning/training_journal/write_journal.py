#!/usr/bin/python3

import sys
from string import Template
import datetime

replacements = {}
to_be_replaced = ['date', 'exercise1', 'warm_set_name1', 'warm_reps1', 'work_set_name1', 'work_reps1', 'exercise2', 'warm_set_name2', 'warm_reps2', 'work_set_name2', 'work_reps2']
to_replace = [datetime.datetime.now().strftime("%A, %m/%d/%Y %H:%M"), *sys.argv[1:]]
replacements = dict(zip(to_be_replaced, to_replace))

with open('template.md', 'r') as f:
    temp = f.read()

out_journal = Template(temp).substitute(replacements)

with open('training_journal.md', 'r+') as outf:
    content = outf.read()
    outf.seek(0, 0)
    outf.write(out_journal + content)
