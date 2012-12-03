import win32com.client

PHONE_FIELDS = ['BusinessTelephoneNumber',
                'HomeTelephoneNumber',
                'MobileTelephoneNumber',
                #'AssistantTelephoneNumber',
                #'OtherTelephoneNumber',
                #'PrimaryTelephoneNumber',
            ]

NAME_FIELDS = ['FullName',
                'CompanyName',
            ]


class MSOutlook(object):
    def __init__(self):
        self.outlookFound = 0
        try:
            self.oOutlookApp =\
            win32com.client.gencache.EnsureDispatch("Outlook.Application")
            self.outlookFound = 1
        except:
            print "unable to load Outlook"
        self.records = []

    def get_contacts(self, group=None):
        if not self.outlookFound:
            return
        mapi = self.oOutlookApp.GetNamespace("MAPI")
        ofContacts =\
        mapi.GetDefaultFolder(win32com.client.constants.olFolderContacts)
        for oc in range(len(ofContacts.Items)):
            contact = ofContacts.Items.Item(oc + 1)
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
                    self.records.append(record)
        return self.records
