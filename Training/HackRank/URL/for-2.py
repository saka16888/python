#import urllib  #error
import urllib.request

Urls = [
    'http://yahoo.com',
    'http://python.org',
    'http://gimp.org',    # The GNU image manipulation program
    ]

def walk(url_list):
    for url in url_list:
        #f = urllib.urlopen(url)
        req = urllib.request.Request(url)
        f = urllib.request.urlopen(req)
        stuff = f.read()
        f.close()
        yield stuff

def test():
    for url in walk(Urls):
        print('length: %d' % len(url), )

if __name__ == '__main__':
    test()
