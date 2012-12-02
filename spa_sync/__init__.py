from optparse import OptionParser
import sys
import spa_phone

def main():
    parser = OptionParser()
    parser.add_option("-p", "--provider", dest="provider", default="contacts",
        help="Contact provider to use: contacts | outlook. default=contacts")
    parser.add_option("-g", "--group", dest="group",
        help="OS X Contacts group name to sync")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        print 'usage: spa-sync ip-address'
        print 'Please provide the SPA Phone IP address as first argument'
        sys.exit(2)

    if options.provider == 'contacts':
        from spa_sync.providers.contacts import export
    if options.provider == 'outlook':
        from spa_sync.providers.outlook import export

    contacts = export(options.group)
    spa_phone.write(args[0], contacts)
    print 'Synced', len(contacts), 'entries'
