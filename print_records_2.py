from pymarc import MARCReader
import re

class MarcProcessor:
    def __init__(self, file_path=r"C:\Users\megrust\Desktop\py4e\match_game\BIBREPORT_2026070618_103979671530006381_new.mrc"):
        self.file_path = file_path

    def process_all_records(self):
        """Opens the file and loops through every record sequence."""
        # 'rb' mode is required as MARC files are binary data
        with open(self.file_path, 'rb') as data_file:
            reader = MARCReader(data_file)
            for record in reader:
                if record is None:
                    continue  # Safely skip badly formatted records
                self.process_single_record(record)
        
    def process_single_record(self, record):
        #Get titles
        title = record.title
        normtitle = re.sub(r'[^A-Za-z0-9]', ' ', title)
        normtitle = re.sub('\\s{2,8}', ' ', normtitle)
        shorttitle = normtitle.lower()[0:30]
       
        
        #Get MMSid
        sysnum = record['001'].value()
        
        #Get ISSN
        output = []
        fields = record.get_fields('022')
        for f in fields:
            for s in f.subfields:
                if s.code == "a":
                    s = re.sub(r'\D', '', s.value)
                    output.append(s)
        if len(output) > 0:
            all_issns = '|'.join(output)
        else:
            all_issns = ''
        
        #Get subjects
        subjects = []
        subjs = record.get_fields('650','610')
        for j in subjs:
            j = re.sub(r'[^A-Za-z0-9]', ' ', j.value())
            j = re.sub('\\s{2,8}', ' ',j)
            subjects.append(j)
        if len(subjects) > 0:
            all_subjs = ' '.join(subjects)
            all_subjs = all_subjs.lower()
        else:
            all_subjs = ''
        
        print(f'{shorttitle}\t{sysnum}\t{all_issns}\t{all_subjs}')
        
        
        
if __name__ == "__main__":        
    processor = MarcProcessor("BIBREPORT_2026070618_103979671530006381_new.mrc")
    processor.process_all_records()