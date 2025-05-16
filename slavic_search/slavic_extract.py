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
    def format(self):
        return(f'FMT:BK')

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
    def title_h(self):
        field = self.record.get_fields('245')
        for f in field:
            for s in f.subfields:
                if s.code == "h":
                    return(s.value)
                else:
                    return ''
    

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
        else:
            return ''
    
    @property
    def isbn(self):
        z = []
        fields = self.record.get_fields('020')
        for f in fields:
            for s in f.subfields:
                if s.code == "a":
                    z.append(f'ISBN:{s.value}')
        if len(z) >= 0:
            all_isbns = '\t'.join(z)
            return all_isbns

    @property
    def issn(self):
        output = []
        fields = self.record.get_fields('022')
        for f in fields:
            for s in f.subfields:
                if s.code == "a":
                    output.append(f'ISSN:{s.value}')
        if len(output) > 0:
            all_issns = '\t'.join(output)
            return all_issns
        else:
            return ''

    @property
    def oclc(self):
        output = []
        fields = self.record.get_fields("035")
        if fields:
            for f in fields:
                for s in f.subfields:
                    if s.code == "a" and re.search("OCoLC", s.value):
                        all_digits = re.findall(r"\d+", s.value)[0]
                        output.append(re.sub(r"^[0]+", r"", all_digits))
        if len(output) > 0:
            return(f'OCLC:{output[0]}')
        else:
            return ''
    
    def all_keys(self):
        x = []
        x.append(f'{self.reckey}')
        x.append(f'FMT:BK')
        x.append(f'{self.language}')
        x.append(f'{self.title}')
        x.append(f'{self.author}')
        x.append(f'{self.author_tag}')
        x.append(f'{self.pubyear}')
        x.append(f'TITLE_H:{self.title_h}')
        x.append(f'{self.publisher}')
        x.append(f'{self.arrival_date}')
        x.append(f'{self.isbn}')
        x.append(f'{self.issn}')
        x.append(f'{self.oclc}')
        keys = '\t'.join(filter(None, x))
        return(keys)
    
    def search_keys(self):
        return self.all_keys
    