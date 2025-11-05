#!/usr/bin/env python


import os
import random


from mastodon import Mastodon


if __name__ == '__main__':
    mastodon = Mastodon(
            #client_id=config.client_id,
            #client_secret=config.client_secret,
            #access_token=config.access_token,
        access_token = 'token.secret',
        api_base_url = 'https://mastodon.social/',
    )
    #mastodon.log_in(config.email, config.password)
    bot_home = os.path.dirname(__file__)
    parts1 = []
    parts2 = []
    with open(os.path.join(bot_home, 'captions.txt')) as f:
        for line in f:
            line = line.rstrip()
            part1, part2 = line.split('\t')
            parts1.append(part1)
            parts2.append(part2)
    part1 = random.choice(parts1)
    part2 = random.choice(parts2)
    text = '{}: {}'.format(part1, part2)
    print(text)
    mastodon.toot(text)
