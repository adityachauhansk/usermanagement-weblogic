from weblogic.management.security.authentication import UserReaderMBean
from weblogic.management.security.authentication import GroupReaderMBean
from weblogic.management.security.authentication import MemberGroupListerMBean

#Run Command: java weblogic.WLST userList.py

# Supply Admin Credentials

adminURL=" "
adminUserName=" "
adminPassword=" "
userNameWildcard="*"
maximumToReturn="0"
showAllAuthenticatorUserList="false"

# Connect to Weblogic in online mode
connect(adminUserName, adminPassword, adminURL)
print("Successfully Connected to Weblogic!")

# Get Security Realm name and authprovider configuration 
realmName=cmo.getSecurityConfiguration().getDefaultRealm()
#print(realmName)
authProvider = realmName.getAuthenticationProviders()
#print(authProvider)
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
#print(atnr)

for i in authProvider:
    if isinstance(i,UserReaderMBean):
        userName = i
        authName= i.getName()

        if authName == 'DefaultAuthenticator':
            userList = i.listUsers(str(userNameWildcard),int(maximumToReturn))
            print 'List of USERS in : "'+authName+'"'
            print '======================================================================'

            num=1
            while userName.haveCurrent(userList):
                
                print userName.getCurrentName(userList) + ' ,',
                print userName.getUserDescription(userName.getCurrentName(userList)),
                print ',',
                g = atnr.listMemberGroups(userName.getCurrentName(userList))
                groupReader = i
                while groupReader.haveCurrent(g):
                    print groupReader.getCurrentName(g) + ' ;',
                    groupReader.advance(g)
                groupReader.close(g)

                print '\n'

                userName.advance(userList)
