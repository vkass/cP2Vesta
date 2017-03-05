#!/usr/bin/python3
import yaml, MySQLdb, getpass, sys, os

if len(sys.argv) < 2:
    sys.exit('Usage: %s <GRANTS_USER.YAML>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: File %s was not found!' % sys.argv[1])

rootpw=getpass.getpass("Enter mysql root password: ")

# Open database connection
connection = MySQLdb.connect("localhost", "root", rootpw, "mysql")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

with open("databases/grants_demoe3.yaml", 'r') as yamlfile:
    for users in yaml.load(yamlfile)['MYSQL'].values():
        for user, grants in users.items():
            for grant in grants:
                cursor.execute(grant);

# disconnect from database
connection.close()
