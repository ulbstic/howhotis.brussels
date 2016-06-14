# How hot is .brussels?

This repo contains the scripts made and used for the paper "How hot is .brussels", whose preprint is available at [howhotis.brussels](http://howhotis.brussels). 

## Overview

#### redirect.sh
This shell script checks whether one URL points to another. Using a two-column *.csv file as input, it uses curl to see if the URL in column 1 is being redirected to the URL in column 2. By putting the same URL in each column of the *.csv file, it becomes possible to determine if there is a redirection or not. 


#### whois_dotbrussels.sh
This shell script launches the whois command on the list of registered .brussels domain names (as of March 2016). You will need to change your IP every 60 domain names for the script not to fail. The results are printed out in stdout and can be parsed using the below python program. 
Download: here

#### parsing_whois.py
This python 2.7 program parses the result of the above program, where each individual result has been encapsulated in the pair of tags. It prints in stdout two columns, the first one containing the domain name and the second one containing the name, address, postal code and city of the registrant.

