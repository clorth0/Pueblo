#!/usr/local/bin/python

import pueblo

PARAMS = {
	'DIR': '/Users/matt/Documents/GitHub/www-odnd',
	'TEMPLATE_DIR': '/Users/matt/Documents/GitHub/www-odnd/Pueblo/templates',
	'IGNORE_LIST': ['ignorethis.txt'],
	'PAGEBUILD_DELTA': 30
	}

print "Content-type: text/html\n\n"

site = pueblo.Site()
site.build_site(PARAMS)

print "<html><head><title>Site Rebuilt</title></head><body><h1>Security Consulting</h1></body></html>"

