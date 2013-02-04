# -*- coding: utf-8 -*-
# Documentation: http://docs.basex.org/wiki/Clients
#
# Usage: BASEX_SERVER=localhost BASEX_USER=admin BASEX_PASS=admin python populate_database.py
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


def CreateGlos(directory = ""):
    
    try:
        base_server = os.environ["BASEX_SERVER"]
        base_port = os.environ.get("BASEX_PORT", 1984)
        base_user = os.environ["BASEX_USER"]
        base_pass = os.environ["BASEX_PASS"]
    except:
        raise ValueError("Please set environmental variables %s, %s, and %s" % ("BASEX_SERVER", "BASEX_USER", "BASEX_PASS"))

    # create session
    session = BaseXClient.Session(base_server, base_port, base_user, base_pass)

    session.execute("drop db glos")
    print(session.info())

    print "Importing XML in DIR: '", directory, "'"

    try:
        # create empty database
        session.execute("create db glos")
        print(session.info())
    
        # add document
        for root, dirs, files in walk(directory):
            for f in files:

                if os.path.splitext(f)[1][1:].strip().lower() != "xml":
                  continue
                
                fpath = join(root,f)
                dbpath = join(root,f)[len(directory):]
                
                #print "File:", fpath
                #print "bd path:", dbpath
        
                session.add(dbpath, readXml(fpath))
                print(session.info())
    
    
    except Exception as e:
        # print exception
        print(repr(e))
    
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
    #print(type(content))
    
    return content
    
    
CreateGlos("ISOs")

