#!/usr/bin/python3

import sys
from string import Template
import datetime

replacements = {}

replacements['date'] = datetime.datetime.now().strftime("%A, %m/%d/%Y %H:%M")
replacements['exercise1'] = sys.argv[1]
replacements['warm_reps1'] = sys.argv[2]
replacements['work_reps1'] = sys.argv[3]
replacements['exercise2'] = sys.argv[4]
replacements['warm_reps2'] = sys.argv[5]
replacements['work_reps2'] = sys.argv[6]

with open('template.md', 'r') as f:
    temp = f.read()

out_journal = Template(temp).substitute(replacements)

with open('training_journal.md', 'r+') as outf:
    content = outf.read()
    outf.seek(0, 0)
    outf.write(out_journal + content)
