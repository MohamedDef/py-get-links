#!/usr/bin/python3

import urllib2

site=input('Enter your page web: ')
open_site = urllib2.urlopen(site)
page=open_site.read()


def link(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    url_start = page.find('"',start_link+5 )
    url_end = page.find ('"',url_start+1)
    url= page[url_start+1:url_end]
    return url, url_end

def all_links(page):
    while True:
        url, end_url = link(page)
        if url: 
            print (url)
            page=page[end_url:]
        else:
            break

all_links(page)