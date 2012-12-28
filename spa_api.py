import re
import unicodedata
from mechanize import urlopen, ParseResponse, TextControl

def read(ip):
    form, controls = _get_controls(ip)
    p = re.compile('^n=(.+?);p=(.+?)(|;r=(.+?))$')
    phonebook = []
    for control in controls:
        m = p.match(control.value)
        if m:
            phonebook.append((m.group(1), m.group(2), m.group(4)))
    return phonebook

def write(ip, phonebook):
    form, controls = _get_controls(ip)
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
            number = re.sub('[^\d+]', '', entry[1])
            control.value = 'n=%s;p=%s' % (name, number)
            if len(entry) == 3 and entry[2]:
                control.value += ';r=%s' % entry[2]
        except IndexError:
            control.value = ''
    urlopen(form.click())

def _get_controls(ip):
    response = urlopen('http://%s/pdir.htm' % ip)
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[0]
    controls = [control for control in form.controls
                if isinstance(control, TextControl)]
    return form, controls
