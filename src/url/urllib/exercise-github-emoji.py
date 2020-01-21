# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import os
import random
import time

def download_all_emojis_on_github_with_urllib():
    '''
    Lists all the emojis available to use on GitHub and then download them.
    '''
    response = urllib2.urlopen('https://api.github.com/emojis')
    result = response.read()
    result = json.loads(result)
    for key,value in result.items():
        filename = key + value[value.rindex('.'):value.rindex('?')]
        filename = './images/github-emoji-{filename}'.format(filename=filename)
        if os.path.exists(filename) is False:
            urllib.urlretrieve(value,filename)
            time.sleep(random.randint(300, 30000))

if __name__ == '__main__':
    print '>>>Download all the emojis available to use on GitHub.<<<'
    download_all_emojis_on_github_with_urllib() 





