#!/usr/bin/env python
import json
import sys
from bioblend import galaxy

history_id=None

if len(sys.argv) < 3:
  print "Usage: %s <host> <APIkey> [optional history_id]" % sys.argv[0]
  sys.exit(1)
elif len(sys.argv) == 3:
  pass
elif len(sys.argv) == 4:
  history_id=sys.argv[3]
else:
  print "Usage: %s <host> <APIkey> [optional history_id]" % sys.argv[0]
  sys.exit(1)

gi = galaxy.GalaxyInstance(url=sys.argv[1], key=sys.argv[2])
hl = gi.histories.get_histories(history_id=history_id)

print json.dumps(hl)
