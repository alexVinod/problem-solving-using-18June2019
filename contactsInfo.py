contacts={}
def addContacts(name, phone):
    # Verify the contact doesn't already exist
    if name not in contacts:
        contacts[name] = phone
        print("New contact added")
    else:
        l=[]
        getP=contacts.get(name)
        print(getP)
        newP=contacts.get(phone)
        l.extend([getP,newP])
        contacts[name]=l
        print(contacts[name])
        # print("Contact %s already exists" % name)
    return
name=input("Name :")
phone=input("Phoe :")
addContacts(name,phone)
print(contacts)
