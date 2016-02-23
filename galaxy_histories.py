#!/usr/bin/env python
import json
import sys
from bioblend import galaxy

if len(sys.argv) != 3:
  print "Usage: %s <host> <APIkey>" % sys.argv[0]
  sys.exit(1)


gi = galaxy.GalaxyInstance(url=sys.argv[1], key=sys.argv[2])

hl = gi.histories.get_histories()

print json.dumps(hl)

