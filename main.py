import re

#email = "example@gmail.com"

listemail=['janedoe@gmail.com',
'johnsmith@yahoo.com',
'michaelb@hotmail.com',
'sarahm@outlook.com',
'alexp@aol.com',
'jennifert@gmail.com',
'kylew@gmail.com',
'chrisb@yahoo.com',
'amandaj@hotmail.com',
'matthewc@outlook.com']

L_username=[]
L_domain=[]

for email in listemail:
    match = re.search(r'([\w.-]+)@([\w.-]+)', email)
    username = match.group(1)
    domain = match.group(2)
    print("Username: ", username)
    print("Domain: ", domain)
    print("\n")
    L_username.append(username)
    L_domain.append(domain)

print("List of username :",L_username)
print("List of domain :",L_domain)


