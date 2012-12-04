import sys
import win32com.client

PHONE_FIELDS = ['BusinessTelephoneNumber',
                'HomeTelephoneNumber',
                'MobileTelephoneNumber']
                 #'AssistantTelephoneNumber',
                 #'OtherTelephoneNumber',
                 #'PrimaryTelephoneNumber',
NAME_FIELDS = ['FullName',
               'CompanyName']


def get_contacts(group=None):
    try:
        outlook_app =\
            win32com.client.gencache.EnsureDispatch("Outlook.Application")
        mapi = outlook_app.GetNamespace("MAPI")
        contacts =\
            mapi.GetDefaultFolder(win32com.client.constants.olFolderContacts)
    except:
        print ("Error: Problems loading Outlook addressbook.")
        sys.exit()
    records = []
    for idx in range(1, len(contacts.Items)):
        contact = contacts.Items.Item(idx)
        if contact.Class == win32com.client.constants.olContact:
            record = {}
            for key in NAME_FIELDS:
                record[key] = getattr(contact, key)
                record['Phones'] = {}
                for pkey in PHONE_FIELDS:
                    value = getattr(contact, pkey)
                    if value:
                        record['Phones'][pkey] = value
            categories = getattr(contact, 'Categories').split(', ')
            if not group or group in categories:
                records.append(record)
    return records
