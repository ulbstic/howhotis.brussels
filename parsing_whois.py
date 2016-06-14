#!/usr/bin/python
# -*- coding: utf-8 -*-

# This parses the result of a script containing several "whois -H $URL" and prints in stdout two columns, the first one containing the domain name and the second one containing the name, address, postal code and city of the registrant.
# Simon Hengchen - shengche@ulb.ac.be - http://homepages.ulb.ac.be/~shengche

# Made for http://howhotis.brussels


import codecs
import re
import io
import os,glob
from bs4 import BeautifulSoup


f = io.open("file.with.WHOIS.entries.separated.by.'<record></record>'.xml",'r',encoding="utf-8")
soup = BeautifulSoup(f,'lxml')

for records in soup.find_all('record'):
	hit = re.search("Domain Name: (.*)",records.get_text())	
	if hit:
		hit = hit.group(1)
		hit2 = "\""+hit+"\","
		registrant = re.search("Registrant Name: (.*)", records.get_text())
		if registrant:
			registrant2 = re.search("Registrant Street: (.*)", records.get_text())
			if registrant2:
				registrant3 = re.search("Registrant City: (.*)", records.get_text())
				if registrant3 :
					registrant4 = re.search("Registrant Postal Code: (.*)", records.get_text())
					if registrant4 :
						registrantinfo = "\""+registrant.group(1) + " " +registrant2.group(1) +" "+ registrant4.group(1) + " " +registrant3.group(1)+"\"" 
					print hit2, registrantinfo

