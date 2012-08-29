import sys

for version in ['2.7', '2.6', '2.5']:
    sys.path.append('/System/Library/Frameworks/Python.framework/Versions/'
                    + version + '/Extras/lib/python/PyObjC')

import addressbook

__all__ = ['export', ]

def export(**kwargs):
    """
    Export the contacts for this provider in the correct format
    """
    contacts = []
    for contact in addressbook.all():
        for type, phone in contact.get('phone', []):
            name = ' '.join([contact.get('first', ''),
                             contact.get('last', '')]).strip()
            if len(contact['phone']) > 1:
                name += ' (%s)' % type
            contacts.append((name, phone))
    return contacts
