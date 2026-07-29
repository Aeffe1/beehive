from pymarc import *
import re


class MarcPrint:
    def __init__(self, record=None):
        with open('test_one.mrc', 'rb') as file:
            reader = MARCReader(file)
            for record in reader:
                self.record = record

    @property                        
    def ttl(self):
        title = self.record.title
        normtitle = re.sub(r'[^A-Za-z0-9]', ' ', title)
        normtitle = re.sub('\\s{2,8}', ' ', normtitle)
        return(normtitle)
        
    @property
    def reckey(self):
        sysnum = self.record['001'].value()
        return(f'{sysnum}')
        
    @property
    def issns(self):
        output = []
        fields = self.record.get_fields('022')
        for f in fields:
            for s in f.subfields:
                if s.code == "a":
                    s = re.sub(r'\D', '', s.value)
                    output.append(s)
        if len(output) > 0:
            all_issns = '|'.join(output)
            return all_issns
        else:
            return ''
    
    @property    
    def subjects(self):
        subjects = []
        subjs = self.record.get_fields('650','610')
        for j in subjs:
            j = re.sub(r'[^A-Za-z0-9]', ' ', j.value())
            j = re.sub('\\s{2,8}', ' ',j)
            subjects.append(j)
        if len(subjects) > 0:
            all_subjs = '|'.join(subjects)
            return all_subjs
        else:
            return ''
    
    @property
    def results(self):
        x = []
        x.append(f'{self.reckey}')
        x.append(f'{self.issns}')
        x.append(f'{self.ttl}')
        x.append(f'{self.subjects}')
        allfields = '\t'.join(filter(None, x))
        return(allfields)
    

        
        