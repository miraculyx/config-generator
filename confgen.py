#!/usr/bin/python3
import re, sys
from datetime import datetime
#
script_name = re.sub(r'(^.*[\\/])', '', sys.argv[0])
usage = 'Usage : ' + script_name +' <template-file> <csv-file>'
version = 'Version 4.0, (c) G. Lange, 09/ 2018'
help = script_name + ' is a script for generating Network device\nconfiguirations from a common template file'
#
# Effective inserted parameters after lauching the script
inserted_paramters = len(sys.argv)
#
if (inserted_paramters == 1 ):
  print (usage)
  sys.exit(1)
#  
if (sys.argv[1] == '-v' or sys.argv[1] == '-h'):
  print (usage)
  print (help)
  print (version)
  sys.exit(1)   
#
# Check what time the script started
t1 = datetime.now()
#
template_file = sys.argv[1]   
csv_file = sys.argv[2]  
#
try:
  csvfh = open(csv_file)
except IOError:
	print ("Failed to open file " + csv_file)
	exit(1)
  
#
csv_line_number = 0
#
# Read the CSV file line by line
for csvline in csvfh:
  csvline = re.sub("(\\r|)\\n|$", "", csvline)
  try:
    tmpfile = open(template_file,'r')
  except IOError:
    print ("Failed to open file " + template_file)
    exit(1)
  #
  # In the first line of the CSV we'll find the parameter names (para_name)
  if csv_line_number == 0:
    para_name = csvline.split(',')
    # Modify the parameters for the substitution in the template file
    for i in range(len(para_name)):
      para_name[i] = "{ " + para_name[i] + " }" 
  else:
    para_values = csvline.split(',')
    # Open the Template File in READ-Only Mode 
    tmpfile = open(template_file,'r') 
    # Create the configuration file with the first parameter of the CSV file as the filename
    if ( len(para_values[0]) > 0):
      filename = para_values[0]
      rconfig = open('%s.cfg' %filename, 'w')
      #
      # Read the Template file line by line and replace the parameters with the values (para_values)
      for tmpline in tmpfile:
        # Try to replace the actual line of the Template File with each of the parameters
        # If there is no match, the line remains the same as before.
        if (len(para_name) == (len(para_values))):
          for i in range(len(para_name)):
            tmpline = tmpline.replace(para_name[i], para_values[i])
          rconfig.write(tmpline)
      rconfig.close()
      print ("Configuration generated for " + filename + " in " + filename + ".cfg")
      tmpfile.close()
  csv_line_number = csv_line_number + 1
csvfh.close()
# Check what time the script has been ended
t2 = datetime.now()
# Calculate the time it took to execute the procedure or getting work the Leaf-Switch
total =  t2 - t1
print ('\nElapsed time : ' + str(total))
