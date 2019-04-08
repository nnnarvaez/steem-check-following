![](https://cdn.steemitimages.com/DQmVBWU7UE5AP4yvVnnpDGgj8MubPCcVDdgvCm2opBV3szK/image.png)

# Project Information

A python snippet to check the list of the people you are following optimized to reduce requests on the API nodes.

* Project Name: Check your followee base

### More detail in [This Post](https://steemit.com/steem/@nnnarvaez/do-you-lost-control-of-your-feed)
Do you lost control of your feed?


# Project status:

It works nicely on the command line giving useful information.
```
672 | aytim           |    2.78 SP | posted    264 days ago, last voted:    264 days ago (LOOKS Dead)
673 | meridalionheart |    0.08 SP | posted     49 days ago, last voted:    117 days ago (LOOKS Dead)
674 | gersson         |   31.30 SP | posted    166 days ago, last voted:    166 days ago (LOOKS Dead)
675 | alxmuh          |    0.29 SP | posted    351 days ago, last voted:    343 days ago (LOOKS Dead)
676 | huslein.slash   |  187.86 SP | posted    159 days ago, last voted:    147 days ago (LOOKS Dead)
677 | aitrading.com   |    0.10 SP | posted    285 days ago, last voted:    285 days ago (LOOKS Dead)
678 | princesson      |    5.03 SP | posted     40 days ago, last voted:     40 days ago (LOOKS Dead)
679 | alphajiggy      |    0.08 SP | posted    130 days ago, last voted:    114 days ago (LOOKS Dead)
680 | rogaze          |    1.97 SP | posted     92 days ago, last voted:     87 days ago (LOOKS Dead)
681 | cuddleme        |    2.32 SP | posted    185 days ago, last voted:    178 days ago (LOOKS Dead)
682 | arlettekid      |    1.75 SP | posted     43 days ago, last voted:     39 days ago (LOOKS Dead)

``` 
> Example output

</br>

Next steps maybe integrate into a discord bot to make it available for the non python wise (this will be done if there is feed back and interet from the community, and especially votes) 

* It shows how many days ago the person you are following **voted** or **posted**, and tells you **their SP**, we have seen cases where accounts are abandoned and powered down those belong to vote rings and other nasty stuff. 

* It also has a sub code set for following what you deem dead, this little program is specially useful when you are following thousands of authors.

* It is nicely inline commented so you know what each stage of the code and the different loops do.

* It throttles down initial node requests and then saves a local JSON file to work locally and avoid punching the nodes.

![](https://cdn.steemitimages.com/DQmT8dUT8mejtuF4mAqPLBL8aqHnufYERVGWySVsoTQf1cw/image.png)

```
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

```
