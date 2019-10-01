#!/usr/bin/env bash

head -18 training_journal.md | sed -E '
1,4d
s/^\|//
s/<td rowspan=2>(.{,10})<\/td>/"\1"/g
s/\|warm up\| (.*) \| /"\1" /
s/\|work set\| (.*) \| /"\1" /
s/([0-9].*) \|\|/"\1"/
s/".*\." //
' | paste -s -d ' \\' | sed '
i#!/usr/bin/env bash \n\n./write_journal.py \\
s/\\/ \\\n/g
' > all_glory.tmp

chmod +x all_glory.tmp
