from pymarc import *
import re

class MarcRecords:
        
    def __init__(self, path=None):
        if path:
            with open('setout5.mrc', 'rb') as file:
                reader = MARCReader(file)
                for record in reader:
                    self.record = record
    
    def print_slavic_title(self):
        return(self.record.title)

    @property
    def reckey(self):
        sysnum = self.record['001'].value()
        return(f'SYSNUM:{sysnum}')

    @property
    def language(self):
        field008 = (self.record['008'].value())
        lang = field008[35:38]
        return(f'LANG:{lang}')
    
    @property
    def title(self):
        ttl = (self.record['245'].value())
        return(f'TITLE:{ttl}')

    @property
    def author_tag(self):
        for field_contents in self.record.get_fields('100'):
            tag = field_contents.tag
            return(f'AUTHOR_TAG:{tag}')
        
    @property
    def author(self):
        auth = (self.record['100'].value())
        return(f'AUTHOR:{auth}')

    @property
    def publisher(self):
        pub = (self.record.publisher)
        return(f'IMPRINT:{pub}')
    
    @property
    def pubyear(self):
        date = (self.record.pubyear)
        return(f'DATE:{date}')

    @property
    def arrival_date(self):
        output = []
        fields = self.record.get_fields('974')
        for f in fields:
            for s in f.subfields:
                if s.code == "r":
                    output.append(f'ARRIVAL_DATE:{s.value[0:10]}')
        if len(output) > 0:
            return output[0]
    
    @property
    def isbn(self):
        output = []
        fields = self.record.get_fields('020')
        for f in fields:
            for s in f.subfields:
                if s.code == "a":
                    output.append(f'ISBN:{s.value}')
        if len(output) > 0:
            all_isbns = 't'.join(output)
            return all_isbns
 
    @property
    def oclc(self):
        output = []
        fields = self.record.get_fields("035")
        for f in fields:
            for s in f.subfields:
                if s.code == "a" and re.search("OCoLC", s.value):
                    all_digits = re.findall(r"\d+", s.value)[0]
                    output.append(re.sub(r"^[0]+", r"", all_digits))
        if len(output) > 0:
            return output[0]
        
    def all_titles_and_labels(self):
        return(f'{self.reckey}\tFMT:BK\t{self.language}\t{self.title}\t{self.author}\t{self.author_tag}\t{self.pubyear}\tTITLE_H:\t{self.publisher}\t{self.arrival_date}\t{self.isbn}'
        )
