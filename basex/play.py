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
    
try:
    base_server = os.environ["BASEX_SERVER"]
    base_port = os.environ.get("BASEX_PORT", 1984)
    base_user = os.environ["BASEX_USER"]
    base_pass = os.environ["BASEX_PASS"]
except:
    raise ValueError("Please set environmental variables %s, %s, and %s" % ("BASEX_SERVER", "BASEX_USER", "BASEX_PASS"))

# create session
session = BaseXClient.Session(base_server, base_port, base_user, base_pass)
session.execute("OPEN glos")
print(session.info())

#print session.execute("CREATE INDEX FULLTEXT")
print session.execute("INFO INDEX FULLTEXT")
print(session.info())