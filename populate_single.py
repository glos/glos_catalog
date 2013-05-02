# -*- coding: utf-8 -*-
# Documentation: http://docs.basex.org/wiki/Clients
#
# (C) BaseX Team 2005-12, BSD License
import BaseXClient
from os import walk
from os.path import join
import os
import sys

if sys.version < '3': # i'm testing with Python 2.7.3
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

import xml.dom.minidom


def UpdateSingle(xml_file):
    
    try:
        base_server = os.environ["BASEX_SERVER"]
        base_port = os.environ.get("BASEX_PORT", 1984)
        base_user = os.environ["BASEX_USER"]
        base_pass = os.environ["BASEX_PASS"]
    except:
        raise ValueError("Please set environmental variables %s, %s, and %s" % ("BASEX_SERVER", "BASEX_USER", "BASEX_PASS"))

    print "Importing file: %s" % xml_file

    # create session
    session = BaseXClient.Session(base_server, base_port, base_user, base_pass)
    session.execute("OPEN glos")

    try:
        dbpath = "/".join(xml_file.split("/")[1:])
        session.replace(dbpath, readXml(xml_file))
        print(session.info()) 
    finally:
        # close session
        if session:
            session.close()

def readXml(filename):
    
    # input encoding is utf-16le
    doc = xml.dom.minidom.parse(filename)
    # expat parser will decode it to real unicode, and rewrite processing instruction.
    # so, we can send this (->toxml()) as content for basex, safely.
    content = doc.toxml()
    # str if Python 3.x, unicode if Python 2.x.
    # (both are actually real unicode. (ucs2 or ucs4.))
    print(type(content))
    
    return content
    
    
UpdateSingle("ISOs/In-situ/storet/10070005.xml")

