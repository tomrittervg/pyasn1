#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pyasn1.sf.net/license.html
#
from pyasn1.type import base, tag

class EndOfOctets(base.AbstractSimpleAsn1Item):
    defaultValue = 0
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x00)
        )
endOfOctets = EndOfOctets()
