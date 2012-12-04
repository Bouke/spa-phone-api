from spa_sync.providers.outlook import client


def export(group=None):
    """
    Export the contacts for this provider in the correct format
    """
    contacts = []
    for contact in client.get_contacts(group):
        name = contact['FullName'] or contact['CompanyName']
        for key, value in contact['Phones'].items():
            if len(contact['Phones']) > 1:
                    type = key.replace("TelephoneNumber", "")
                    name += ' (%s)' % type
            contacts.append((name, value))
    return contacts
