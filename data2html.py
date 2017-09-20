#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
csvfile = open('data.csv', 'rb')

reader = csv.reader(csvfile, delimiter=',')

header = reader.next()

header[0] # index #
header[1] # Release 
header[2] # Tag
header[3] # Name
header[4] # Description
header[5] # Valid numeric range
header[6] # Scale interpretation
header[7] # Recommended 'normal' value
header[8] # Suggested programmatic interactions:
header[9] # Suggested user interactions
header[10] # Related axis information
header[11] # Demo
header[12] # Written
header[13] # Edited
header[14] # Glyph
header[15] # Axis Name
header[16] # Video Complete
header[17] # Delivered DC
header[18] # Mantra flag tag

#for i, item in enumerate(header):
#	print "header["+str(i)+"] # "+item

datadict = {}

for row in reader:
	if row[1]: # Release
		index = row[0]
		d = datadict[int(index)] = {}
		d["tag"] = row[2]
		d["name"] = row[3]
		d["description"] = row[4]
		d["valrange"] = row[5]
		d["scaleint"] = row[6]
		d["recomval"] = row[7]
		d["suggprog"] = row[8]
		d["sugguser"] = row[9]
		d["relainfo"] = row[10]

for key, value in datadict.items():
	print '<h3 id="%s">%s. %s</h3>' % (value["tag"].lower(), key, value["tag"])
	print '<p>'
	print '<b>Tag:</b> %s<br>' % value["tag"]
	print '<b>Name:</b> %s<br>' % value["name"]
	print '<b>Description:</b> %s<br>' % value["description"]
	print '<b>Valid numeric range:</b> %s<br>' % value["valrange"]
	print '<b>Scale interpretation:</b> %s<br>' % value["scaleint"]
	print '<b>Recommended ‘normal’ value:</b> %s<br>' % value["recomval"]
	print '<b>Suggested programmatic interactions:</b> %s<br>' % value["suggprog"]
	print '<b>Suggested user interactions:</b> %s<br>' % value["sugguser"]
	print '<b>Related axis information:</b> %s<br>' % value["sugguser"]
	print '</p>'
	print '<h4>Demo</h4>'
	print '<img src="images/animation-%s.gif" />' % value["tag"]
	print
	print '<hr>'
	print
	
csvfile.close()