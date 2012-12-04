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
        print 'usage: spa-sync IP-ADDRESS [--provider PROVIDER] [--group GROUP]'
        print 'Please provide the SPA Phone IP address as first argument'
        sys.exit(2)

    if options.provider == 'contacts':
        from spa_sync.providers.contacts import export
    elif options.provider == 'outlook':
        from spa_sync.providers.outlook import export
    else:
        raise ValueError('Valid providers are: contacts and outlook')

    try:
        contacts = export(options.group)
    except Exception as e:
        print 'Could not get contacts from provider (%s)' % e
    else:
        spa_phone.write(args[0], contacts)
        print 'Synced', len(contacts), 'entries'
