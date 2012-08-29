from optparse import OptionParser
import sys
import spa_phone
from spa_sync.providers.contacts import export

def main():
    parser = OptionParser()
    parser.add_option("-g", "--group", dest="group",
        help="OS X Contacts group name to sync")
    (options, args) = parser.parse_args()

    if len(args) == 0:
        print 'usage: spa-sync ip-address'
        print 'Please provide the SPA Phone IP address as first argument'
        sys.exit(2)

    contacts = export(options.group)
    spa_phone.write(args[0], contacts)
    print 'Synced', len(contacts), 'entries'
