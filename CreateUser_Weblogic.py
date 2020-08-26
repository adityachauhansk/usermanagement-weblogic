from java.io import FileInputStream
from weblogic.management.security.authentication import UserReaderMBean

# Setup the environment needed for WLST: $ source setWLSEnv.sh
# Run Command: wlst.sh createUser.py

#Name of input file 


csv_file=open('userlist.csv', mode='r')
csv_reader = csv_file.read()
csv_file.close()
xrows=csv_reader.rstrip('\n')
rows=xrows.split('\n')

#List comprehension to extract column values from csv except header

uName=[row.split(',')[0] for row in rows[1:]]
passWD=[row.split(',')[1] for row in rows[1:]]
desc=[row.split(',')[2] for row in rows[1:]]


# Supply weblogic Admin Credentials
adminURL='host:port'
adminUserName='consult'
adminPassword='consult12'

#connect to weblogic using supplied credentials
connect(adminUserName, adminPassword, adminURL)

atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider('DefaultAuthenticator')


#Creating users

print ('Creating Users ....')
i=0
for name in uName:
    try:
        atnr.createUser(name,passWD[i],desc[i])
        print ('User '+ name +' created successfully!')
        i = i + 1
    except:
        print ('Error trying to create user ' + name + ' user already exists in the backend!')
~                                                                                                   