#!/usr/bin/env python
# encoding: utf-8
"""
addressbook.py

Python wrapper around Mac OSX Address Book.

from: https://raw.github.com/prabhu/macutils/master/addressbook.py
"""

from AddressBook import *

# List of properties to be ignored.
IGNORED_PROPS = ["com.apple.ABPersonMeProperty", "ABPersonFlags",
                 "com.apple.ABImageData",
                 "com.apple.ABGroupMembersProperty",
                 ]

def getPeopleInAddressBook(group_name=None):
    """
    Returns the people found in the AddressBook.

    optional parameter(group_name = the name of the group)
    """
    ab = ABAddressBook.sharedAddressBook()
    people = None
    if not group_name:
        people = ab.people()
    else:
        for group in ab.groups():
            if group.name() == group_name:
                people = group.members()
    if people == None:
        print "No contacts could be found for given group"
    return _clist(people)


def _clist(slist):
    """
    Method to convert NSArray to python list
    """
    retList = []
    if slist == None:
        return retList
    for p in slist:
        aobj = {}
        for prop in p.allProperties():
            if prop in IGNORED_PROPS:
                continue
            tmpval = p.valueForProperty_(prop)
            if type(tmpval) == ABMultiValueCoreDataWrapper:
                aval = [(_getVal(tmpval.labelAtIndex_(i)),
                         _getVal(tmpval.valueAtIndex_(i)))
                    for i in range(0, tmpval.count())]
            else:
                aval = _getVal(tmpval)
            if aval is not None:
                aobj[prop.lower()] = aval
        retList.append(aobj)
    return retList

def _getVal(tmpval):
    """
    Extract value from unicode, Date or Dictionary object.
    """
    aval = None
    if type(tmpval) == objc.pyobjc_unicode:
        aval = tmpval.lstrip('_$!<').rstrip('>!$_')
    elif issubclass(tmpval.__class__, NSDate):
        aval = tmpval.description()
    elif type(tmpval) == NSCFDictionary:
        aval = dict([(k.lower(), tmpval[k]) for k in tmpval.keys()])
    return aval
