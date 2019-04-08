
from datetime import datetime
from steem import Steem
import time
from steem.account import Account
stm = Steem(keys = "---posting_key---") #  posting STEEMit

account_to_check ='name-of-the-account-whose-followers-will-be-evaluated'

muted_me = stm.steemd.get_followers(account_to_check,start_follower='', follow_type='ignore' ,limit=1000)



max = stm.steemd.get_follow_count(account_to_check)['following_count'] # Get number of followed accounts
i_follow = []
last = '' 

# Loop until all have been fetched
while len(i_follow) < max:
    if_t = stm.steemd.get_following(account_to_check,start_follower=last, follow_type='blog' ,limit=1000)
    i_follow = i_follow + if_t
    last = if_t[-1]['following']
    if_t = []
len(i_follow)


u_r_following={} # initialize Empty JSON


# Populate Json 
# let the nodes rest 5 seconds to avoid discconects
# (It will restart from the last in case the node disconnects)


i = 0 # Make a counter to show during execution

for data in i_follow:
    i= i+1
    print('{} | {} | T/F {}'.format(i,data['following'],data['following'] in u_r_following))
    if data['following'] in u_r_following:
        continue
    else:
        user = Account(data['following'])
        u_r_following.update({data['following']:user})
        time.sleep(5)

# Once we have all the data in the u_r_following JSON
# We save it to a file, since it should not change in real time

import json
data_file = '/home/bear/bots/follow/following.json'
data = json.load(open(data_file ))
json.dump(u_r_following, open(data_file ,'w'))

# Now we have the data in a local file and can let the nodes rest.
# Maybe next run we can load the file and just update it to avoid
# Saturating the nodes ? 

# Lets make a loop to see which accounts have not Voted or commented in X days
# Initialize some useful variables

l_v = 30                     # last vote 30 days ago
l_c = 30                     # last post 30 days ago (in the if we use the hard coded value 10000 for accounts that never posted
end_date = datetime.utcnow() # We get the time now (we are only interested in the date but well)

# Here we initialize conversions that allow to calculate the user's SP
# We only need to get these once at the beggining

tvfs = float(str.split(stm.steemd.get_dynamic_global_properties()['total_vesting_fund_steem'])[0])
tvs = float(str.split(stm.steemd.get_dynamic_global_properties()['total_vesting_shares'])[0])

i = 0                        # initialize a counter
# We address the property of each followee like thi: 
# u_r_following[followed]['last_vote_time']
for followed in u_r_following:
    
    # Let's get the last vote and last comment time
    # and format nicely in days since so we can do some math
    last_vote = datetime.strptime(str(u_r_following[followed]['last_vote_time']), '%Y-%m-%dT%H:%M:%S')
    delta_vote = abs((end_date - last_vote).days)
    last_post = datetime.strptime(str(u_r_following[followed]['last_root_post']), '%Y-%m-%dT%H:%M:%S')
    delta_post = abs((end_date - last_post).days)
    
    # Let's get the user SP to see if he has not taken it all out
    # That is a good indicator he left
    
    followed_vs = float(str.split(u_r_following[followed]['vesting_shares'])[0])
    vestSteem = tvfs / tvs
    followed_sp = followed_vs * vestSteem      
    if delta_post > 10000:
        i = i + 1 # Increase the counter    
        print('{:003} | {:16}|{:8.02f}SP | never posted ( High SP = vote BOT or a Curator | Low SP = likely a fake account'.format(i,followed,followed_sp))    
    # Let's check for accounts that have gone dormant in the last X days 
    # (change l_c & l_v to fine tune)
    # Maybe a run of dormant during 60 days will give you a good indicator 
    # The user has left for good the platform.
    if delta_vote > l_v and l_c < delta_post < 10000: # looks dead to me
        i = i + 1 # Increase the counter
        print('{:003} | {:16}|{:8.02f} SP | posted {:6} days ago, last voted: {:6} days ago (LOOKS Dead)'.format(i,followed, followed_sp, delta_post,delta_vote))

    # Let's check for curators that never post but vote 
    # (sometimes these are fake accounts created to make small vote rings)
    # A good indicator this is a fake account would be that it is old and has almost no SP
    if delta_post > 10000:
            print('{:003} | {:16}|{:8.02f}SP | never posted ( High SP = vote BOT or a Curator | Low SP = likely a fake account'.format(followed,followed_sp))
     
# Get SP of the followed
i = 0
for followed in u_r_following:
    i=i+1
    if u_r_following[followed]['vesting_balance'] != '0.000 STEEM':
        followed,u_r_following[followed]['vesting_shares'],i
     

 
   
# Unfollow everyone
for user in u_r_following:
    stm.commit.unfollow(user , what=['blog'], account=account_to_check)   

i_follow = stm.steemd.get_followers('nnnarvaez',start_follower='', follow_type='blog' ,limit=1000)
i = 0
for data in i_follow:
    i= i +1
    i

    acc.get_account_history(index=-1,start=1, limit=2500, filter_by='transfer', raw_output=False, order=1)
