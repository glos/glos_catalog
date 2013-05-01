from pyiso.utils.etree import etree
from shutil import abspath
import requests
import os
import csv
import tempfile
import codecs

class GeoCollector(object):
    def __init__(self, base_url):
        self.data = base_url + '/srv/en/csv.search?'
        self.download = base_url + '/srv/en/iso19139.xml?id='

    def utf_8_encoder(self, unicode_csv_data):
        for line in unicode_csv_data:
            yield line.encode('utf-8')

    def run(self):

        isos = []

        o, t =  tempfile.mkstemp()
        with codecs.open(t, "w+", "utf-8") as h:
            h.write(requests.get(self.data).text)

        with codecs.open(t, "rb", "utf-8") as f:
            reader = csv.DictReader(self.utf_8_encoder(f), delimiter='\t')
            for row in reader:
                if row.get('schema') != 'iso19139':
                    continue

                download_url = self.download + row.get('id')
                isos.append(download_url)

        os.unlink(f.name)

        return isos
