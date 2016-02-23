#!/usr/bin/env python
import json
import sys
import csv
from bioblend import galaxy
output_format = 'json'

if len(sys.argv) == 5 and sys.argv[4] == '--tsv':
  output_format = 'tsv'

elif len(sys.argv) != 4:
  print "Usage: %s <host> <APIkey> <history_id> (--tsv)" % sys.argv[0]
  sys.exit(1)


gi = galaxy.GalaxyInstance(url=sys.argv[1], key=sys.argv[2])

hl = gi.histories.show_matching_datasets(sys.argv[3])


paramnames = ['hid','history_id','id','state','file_size','file_ext','name','misc_blurb','url',]
header = dict([(val,val)for val in paramnames])
hs=[]
hs.insert(0,header)
for item in hl:
  hi = {}
  if item['deleted']:
    continue
  for param in paramnames:
    hi[param]=item[param]
  hs.append(hi)


if output_format == 'json':
  print json.dumps(hl)
elif output_format == 'tsv':
  writer = csv.DictWriter(sys.stdout,paramnames)
  writer.writerows(hs)

