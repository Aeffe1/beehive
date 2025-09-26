import os
import sys
import re
from datetime import datetime

#This works but needs some refactoring
#python -m pytest get_log_lines_test.py -vv

#  FOR RUNNING PYTEST: comment the sys.argv lines and uncomment the COV and LIB lines. When running it for production, uncomment the print line at the end.
class Constants:
        COV_DATE = '20250519'
        LIB_CODE = 'e8w'
        #COV_DATE = sys.argv[1]
        #LIB_CODE = sys.argv[2]
        PATH = r"C:\Users\megrust\Desktop\Workstuff\OCLC Datasync"

class FileLocation:

    @property
    def pathname(self):
        return(
            f'{Constants.PATH}\\Xrefs-{Constants.COV_DATE}-{Constants.LIB_CODE}'
            ) 
            
    @property
    def input_date(self):
        return(
            f'{Constants.COV_DATE}'
            )
            
            
    # libcode is output - do not delete
    @property
    def libcode(self):
        return(
            f'{Constants.LIB_CODE}'
            )
    
    @property
    def mrc_file_name(self):
        #Look for the relevant files in this directory:
        for (root,dirs,files) in os.walk(f'{self.pathname}'): 
            for file_name in files:
                if ".mrc" in file_name:
                    return(
                        f'{file_name}'
                     )
    
    @property
    def keyfilename(self):
        for (root,dirs,files) in os.walk(f'{self.pathname}'):
            for file_name in files:
                if "keys.txt" in file_name:
                    return(
                        f'{file_name}'
                        )

    @property
    def xreffilename(self):
        for (root,dirs,files) in os.walk(f'{self.pathname}'):
            for file_name in files:
                if "BibCrossRefReport" in file_name:
                    return(
                        f'{file_name}'
                        )                    
                                       
    @property
    def keycount(self):
        for (root,dirs,files) in os.walk(f'{self.pathname}'): 
            for file_name in files:
                if "keys.txt" in file_name:
                    with open(root+"\\"+file_name, "r") as k:
                        for line in k:
                            if "records kept" in line:
                                kcount = re.search(r"\d+", line)

                                return(
                                    int(kcount.group())
                                    )
  
    @property
    def xrefcount(self):
        for (root,dirs,files) in os.walk(f'{self.pathname}'): 
            for file_name in files:
                if "BibCrossRefReport" in file_name:
                    with open(root+"\\"+file_name, "r") as f:
                        line_count = sum(1 for line in f)
                        return(
                            line_count
                            )

    @property
    def reportname(self):
        for (root,dirs,files) in os.walk(f'{self.pathname}'):
            for file_name in files:
                if "_report.txt" in file_name:
                    return(
                        f'{file_name}'
                        )

                                    
    @property
    def report_data(self):
        s = []
        for (root,dirs,files) in os.walk(f'{self.pathname}'):         
            for file_name in files:
                if "_report.txt" in file_name:
                    with open(root+"\\"+file_name, "r") as d:
                        for line in d:
                            if "updates" not in line:
                                digits = re.search(r"\d+", line)
                                dataline = str(digits.group())
                                s.append(dataline)
                        return ('\t'.join(s))
               
               
    @property
    def key_create_date(self):
        c_time = os.path.getctime(f'{self.pathname}\\{self.keyfilename}')
        dt_create = datetime.fromtimestamp(c_time).strftime('%Y%m%d')
        return(
            dt_create
            )
            
    @property
    def xref_create_date(self):
        c_time = os.path.getctime(f'{self.pathname}\\{self.xreffilename}')
        dt_create = datetime.fromtimestamp(c_time).strftime('%Y%m%d')
        return(
            dt_create
            )
    
    @property
    def report_create_date(self):
        c_time = os.path.getctime(f'{self.pathname}\\{self.reportname}')
        dt_create = datetime.fromtimestamp(c_time).strftime('%Y%m%d')
        return(
            dt_create
            )  
    
    @property
    def number_not_returned(self):
        not_returned = int(self.keycount) - int(self.xrefcount)
        return(
            not_returned
            )
    
    
    def reportresult(self):
        s = []
        s.append(f'{self.mrc_file_name}')
        s.append(f'{self.libcode}')
        s.append('bib')
        s.append(f'{self.keycount}')
        s.append(f'{self.input_date}')
        s.append(f'{self.key_create_date}')
        s.append(f'{self.xref_create_date}')
        s.append(f'{self.xrefcount}')
        s.append(f'{self.number_not_returned}')
        s.append(f'{self.report_create_date}')
        s.append(f'{self.report_data}')
        stats = '\t'.join(filter(None, s))
        return(stats)
       
    
#print(FileLocation().reportresult())