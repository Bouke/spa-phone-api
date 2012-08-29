import sys

for version in ['2.7', '2.6', '2.5']:
    sys.path.append('/System/Library/Frameworks/Python.framework/Versions/'
                    + version + '/Extras/lib/python/PyObjC')

from spa_sync.providers.contacts import addressbook

__all__ = ['export', ]

def export(group=None):
    """
    Export the contacts for this provider in the correct format
    """
    contacts = []
    for contact in addressbook.getPeopleInAddressBook(group_name=group):
        num_phones = 0
        for type, phone in contact.get('phone', []):
            if not 'fax' in type.lower():
                num_phones += 1
        for type, phone in contact.get('phone', []):
            if 'fax' in type.lower():
                continue
            name = ' '.join([contact.get('first', ''),
                             contact.get('middle', ''),
                             contact.get('last', '')]).strip()
            if name == '':
                name = contact.get('organization', '')
            if num_phones > 1:
                name += ' (%s)' % type
            contacts.append((name, phone))
    return contacts
