=============
SPA Phone API
=============

SPA Phone API provides an API for Linksys/Sipura SPA IP Phones. It can be used
to programmatically update the phone's address book. Combining it into other
scripts it can be used build scripts that sync the phone's address book with
Google Contacts or CRM services.


Installation
============

Installation with ``pip``:
::

    $ pip install spa-phone-api


Usage
=====

Read the address book
::

    import spa_api
    spa_api.read('10.0.1.8')

Update the address book
::

    import spa_api
    spa_api.write('10.0.1.8', [
        ('Bouke Haarsma', '+31508200267'),
        ('WebAtoom', '+31508200267'),
        ('Apple Store', '+18006927753'),
    ])


Contributions
=============

Contributions welcome!
