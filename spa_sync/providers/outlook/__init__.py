from spa_sync.providers.outlook.client import MSOutlook


def export(group=None):
    """
    Export the contacts for this provider in the correct format
    """
    contacts = []
    ms_client = MSOutlook()
    for contact in ms_client.get_contacts(group):
        name = contact['FullName'] or contact['CompanyName']
        for key, value in contact['Phones'].items():
            if len(contact['Phones']) > 1:
                    type = key.replace("TelephoneNumber", "")
                    name += ' (%s)' % type
            contacts.append((name, value))
    return contacts
