from peewee import *
from datetime import date
from create import *
from read import *
from update import *
from delete import *

db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

# \n == LINE BREAK


class BaseModel(Model):

    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    address = CharField()
    phone = CharField(max_length=10)
    email = CharField()
    # social_media = CharField()

# class Name(BaseModel):
#     first = CharField()
#     last = CharField()

class Address(BaseModel):
    name = CharField()
    street = CharField()
    city = CharField()
    state = CharField()
    zip_code = CharField()

class Phone(BaseModel):
    name = CharField()
    home = CharField(max_length=10)
    cell = CharField(max_length=10)
    work = CharField(max_length=10)

class SocialMedia(BaseModel):
    name = CharField()
    twitter = CharField()
    facebook = CharField()
    instagram = CharField()
    snapchat = CharField()

db.connect()
db.drop_tables([Contact])
# db.drop_tables([Name])
db.drop_tables([Phone])
db.drop_tables([SocialMedia])
db.create_tables([Contact])
# db.create_tables([Name])
db.create_tables([Phone])
db.create_tables([SocialMedia])

# CREATE
tom = Contact(first_name='Thomas', last_name='Wayne', address='123 Gotham Alley', phone='0000000000', email='tom@mailbox.org')
harvey = Contact(first_name='Harvey', last_name='Dent', address='Two Face Place', phone='7162375934', email='hdent24@gothamDAoffice.org')
jonathan = Contact(first_name='Johathan', last_name='Crane', address='000 Lunatic st', phone='0909090909', email='drcrane@arkham.org')
# Setup Phone
# Setup SocialMedia
bob = Contact(first_name='Robert', last_name='Paulson', address='456 B st', phone='5859385758', email='robertpaulson@fightclub.com')
bill = Contact(first_name='Bill', last_name='Murray', address='34 Venkman Place', phone='1098765432', email='drvenkman@ghostbusters.com')
barry = Contact(first_name='Barry', last_name='HBO', address='9 Sunday Night Way', phone='5858888888', email='billhader@greatshow.com')
# Setup Phone
# Setup SocialMedia
joe = Contact(first_name='Joseph', last_name='Shmoe', address='789 C st', phone='2027384905', email='joeshmoe@lollygag.co')
john = Contact(first_name='John', last_name='Connor', address='1997 Judgement Day Circle', phone='worldsend', email='johnconnor@1991.T2')
jimmy = Contact(first_name='Jim', last_name='Morrison', address='71 Doors blvd', phone='0909090909', email='whenurastranger@kilmer.com')
jerry = Contact(first_name='Jerry', last_name='Rice', address='49 Haight st', phone='6500848990', email='bestreceiver@fris.co')
# Setup Phone
# Setup SocialMedia
guy = Contact(first_name='Guy', last_name='People', address='1234 Place Way', phone='0912873477', email='guy@mail678.org')
greg = Contact(first_name='Gregory', last_name='Peck', address='56789 Location Ave', phone='9998887777', email='gp@yahoo.org')
gregor = Contact(first_name='Gregor', last_name='Mountain', address='111 Cersei Place', phone='0000000000', email='themountain@imazombieorg')

tom.save()
harvey.save()
jonathan.save()
bob.save()
bill.save()
barry.save()
joe.save()
john.save()
jimmy.save()
jerry.save()
guy.save()
greg.save()
gregor.save()

# print(f"{tom.first_name}  {tom.last_name}  {tom.address}  {tom.phone}  {tom.email}")
# print(f"{bob.first_name}  {bob.last_name}  {bob.address}  {bob.phone}  {bob.email}")
# print(f"{joe.first_name}  {joe.last_name}  {joe.address}  {joe.phone}  {joe.email}")

# READ (.get() and .select())

def get_info_by_first():
    print(' ')
    print('RETRIEVE CONTACT INFORMATION')
    print('Enter the person`s first name')
    print(' ')
    person = input('first name: ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    try:
        if Contact.first_name == person:
            reply = Contact.get(Contact.first_name == person)
            print("CONTACT INFORMATION")
            print(f"Name: {reply.first_name} {reply.last_name}")
            print(f"Address: {reply.address}")
            print(f"Phone: {reply.phone}")
            print(f"Email: {reply.email}")
    finally:
        print(' ')
        # print('INVALID RESPONSE')
        # input('Press ENTER to try again')
        get_info_by_first()
    # else:
    #     prompt_options()

def see_all_contacts():
    contacts = Contact.select()
    for i in contacts:
        print(' ')
        print('ENTRY')
        print(f"Name: {i.last_name}, {i.first_name}")
        # print(f"Last name: {i.last_name}")
        print(f"Address: {i.address}")
        print(f"Phone number: {i.phone}")
        print(f"Email: {i.email}")
        print(f"ID: {i.id}")

def see_all_contacts_with_option():
    contacts = Contact.select()
    for i in contacts:
        print(' ')
        print('ENTRY')
        print(f"Name: {i.last_name}, {i.first_name}")
        print(f"Address: {i.address}")
        print(f"Phone number: {i.phone}")
        print(f"Email: {i.email}")
        # print(f"Email: {i.id}")
    print('')
    print('FIND YOUR CONTACT')
    print('')
    input('press ENTER to return to update')
    update_info_by_first()

# UPDATE

def update_info_by_first():
    print(' ')
    print('UPDATE CONTACT PHONE NUMBER')
    print('Enter the person`s first name')
    print(' ')
    person = input('first name: ')
    new_phone = input('New phone number: ')
    try:
        reply = Contact.get(Contact.first_name == person)
        reply.phone = new_phone
        reply.save()
    finally:
        print(' ')
        print('INVALID RESPONSE')
        input('Press ENTER to try again')
        update_info_by_chioice()

def update_info_by_choice():
    print(' ')
    print('UPDATE CONTACT PHONE NUMBER')
    step1 = input('Enter S to submit a query or A to see all contacts: ')
    if step1 == 'S':
        print(' ')
        person = input('first name: ')
        new_phone = input('New phone number: ')
        try:
            reply = Contact.get(Contact.first_name == person)
            reply.phone = new_phone
            reply.save()
        finally:
            print(' ')
            print('INVALID RESPONSE')
            input('Press ENTER to try again')
            update_info_by_choice()
    elif step1 == 'A':
        see_all_contacts_with_option()
    else:
        print(' ')
        print('INVALID RESPONSE')
        input('Press ENTER to return home')
        prompt_options()

    
# DELETE

def delete_contact_by_first():
    print(' ')
    print('REMOVE CONTACT')
    print('Enter the person`s first name')
    print(' ')
    person = input('first name: ')
    print(' ')
    try:
        reply = Contact.get(Contact.first_name == person)
        print("CONTACT INFORMATION")
        print(f"Name: {reply.first_name} {reply.last_name}")
        print(f"Address: {reply.address}")
        print(f"Phone: {reply.phone}")
        print(f"Email: {reply.email}")
        print(' ')
        yes_no = input(f"Are you sure you want to delete the contact info for " + person + "? Y or N: ")
        if yes_no == 'Y':
            reply = Contact.get(Contact.first_name == person)
            reply.delete_instance()
        elif yes_no == 'N':
            print(' ')
            input('Press ENTER to return home')
            prompt_options()
        else:
            print(' ')
            print('INVALID RESPONSE')
            input('Press ENTER to return home')
            prompt_options()
    finally:
        print(' ')
        print('INVALID RESPONSE')
        input('Press ENTER to try again')
        delete_contact_by_first()
# CREATE

def add_contact(first_name, last_name, address, phone, email):
    print(' ')
    print('CREATE NEW CONTACT')
    print('if you have nothing to enter for a field press ENTER.')
    print(' ')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    address = input('Address: ')
    phone = input('Phone: ')
    email = input('Email: ')
    # phone = input('Social Media: ')

    first_name = Contact(first_name=first_name, last_name=last_name, address=address, phone=phone, email=email)
    first_name.save()
    



# NAVIGATION FUNCTION

def prompt_options():
    print(' ')
    print('WELCOME TO CONTACTS: PLEASE CHOOSE FROM THE FOLLOWING OPTIONS')
    print('Enter C to create a contact')
    print('Enter G to get a single contact`s info')
    print('Enter A to get all contacts` info')
    print('Enter U to update a contact')
    print('Enter D to delete a contact')
    print('Enter Q to exit')
    print(' ')
    action = input('ACTION: ')
    if str(action) == 'C':
        add_contact('first_name', 'last_name', 'address', 'phone', 'address')
        print('Contact created!')
        prompt_options()
    elif str(action) == 'G':
        get_info_by_first()
        print(' ')
        input('Hit ENTER to return home')
        prompt_options()
    elif str(action) == 'A':
        see_all_contacts()
        print(' ')
        input('Press ENTER to navigate to home screen')
        prompt_options()
    elif str(action) == 'U':
        update_info_by_choice()
        print('Contact phone number updated!')
        prompt_options()
    elif str(action) == 'D':
        delete_contact_by_first()
        print('Contact deleted!')
        prompt_options()
    elif str(action) == 'Q':
        exit()
    else:
        print(' ')
        print('INVALID RESPONSE')
        prompt_options()



prompt_options()
# see_all_contacts()






# FUNCTION CALLS

# CREATE
# add_contact('first_name', 'last_name', 'address', 'phone', 'address')

# GET ONE CONTACT
# get_info_by_first()

# DELETE
# delete_contact_by_first()

# UPDATE PHONE NUMBER
# update_info_by_first()

# GET ALL CONTACTS
# see_all_contacts()