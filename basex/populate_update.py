import os
import sys
import xml.dom.minidom

import BaseXClient

def readXml(filename):
    doc = xml.dom.minidom.parse(filename)
    content = doc.toxml()    
    return content

def main(directory="../ISOs", include_files=None):

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

    print "Updating XML from DIR: '", directory, "'"

    try:   
        for root, dirs, files in os.walk(directory):
            print root
            for f in files:

                if os.path.splitext(f)[1][1:].strip().lower() != "xml":
                  continue
                
                fpath = os.path.join(root,f)
                dbpath = os.path.join(root,f)[len(directory):]

                # Only process files that contain the string 'include_files'
                if include_files is not None:
                    if include_files not in dbpath:
                        continue

                print "Updating %s..." % dbpath
                session.replace(dbpath, readXml(fpath))
    
    except Exception as e:
        print(repr(e))
    
    finally:
        # close session
        session.execute("CREATE INDEX FULLTEXT")
        if session:
            session.close()

directory = None
if sys.argv[1] is not None:
    directory = sys.argv[1]
    
files = None    
if sys.argv[2] is not None and sys.argv[2].lower() != "all":
    files = sys.argv[2]

main(directory=directory, include_files=files)

