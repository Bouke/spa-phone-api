import re
import unicodedata

__all__ = ['read', 'write']

from mechanize import urlopen, ParseResponse, TextControl

def parse(ip):
    response = urlopen('http://%s/pdir.htm' % ip)
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[0]
    controls = [control for control in form.controls
                if isinstance(control, TextControl)]
    return form, controls

def read(ip):
    form, controls = parse(ip)
    p = re.compile('^n=(.+?);p=(.+?)(|;r=(.+?))$')
    phonebook = []
    for control in controls:
        m = p.match(control.value)
        if m:
            phonebook.append((m.group(1), m.group(2), m.group(4)))
    return phonebook

def write(ip, phonebook):
    form, controls = parse(ip)
    if len(phonebook) > len(controls):
        raise OverflowError('Too many entries provided (max %d)'
            % len(controls))
    for idx, control in enumerate(controls):
        try:
            entry = phonebook[idx]
            if not 2 <= len(entry) <= 3:
                raise ValueError('Phone book entries should have 2 or 3 values')
            name = unicodedata.normalize('NFKD', entry[0]).encode('ascii',
                                                                  'ignore')
            control.value = 'n=%s;p=%s' % (name, entry[1])
            if len(entry) == 3 and entry[2]:
                control.value += ';r=%s' % entry[2]
        except IndexError:
            control.value = ''
    urlopen(form.click())
