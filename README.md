# config-generator
Python Script to generate network devices configuration files form a template and a CSV File.

All parameters of an CSV file have to be terminated by these kind of brakets: {}
The parameter hostname in the CSV File has to be inserted as { hostname }
as a variable for other devices.
There is no limit of the possible varibales you can use in your template.

confgen.py {template-file} {csv-file}
