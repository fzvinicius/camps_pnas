# Selecting users ids for initial 'user_indo' sampling
import random

random.seed(3004)

MIN_ID = 1
MAX_ID = int(2e9)           # 2B
INTERVAL_SIZE = int(1e7)    # 10M 
SAMPLE_SIZE = int(1e4)      # 10K

sample_idx = 1
cur_id = MIN_ID
uids = []
while cur_id < MAX_ID:
    print 'At', sample_idx
    ini_id = cur_id
    end_id = cur_id + INTERVAL_SIZE
    sampled_ids = random.sample(range(ini_id, end_id), SAMPLE_SIZE)
    
    uids += sampled_ids
    sample_idx += 1
    cur_id += INTERVAL_SIZE


print 'sampled', len(uids)
uids = map(str,uids)
with open('sampled_2M_users.txt', 'w') as out:
    out.write('\n'.join(uids))

