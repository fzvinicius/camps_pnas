#!/usr/bin/python
# -*- coding: iso-8859-1 -*-


import json
data = open("sampled_2M_users.txt", "r")

d = {}
uids = []
for i, line in enumerate(data):
    uid = line.strip()
    d['id'] = uid
    d['status'] = '0'
    d['info'] = 'null'
    uids.append(json.dumps(d))

out = open('sampled_2M_users.json', 'w')
out.write('['+',\n'.join(uids)+']')
