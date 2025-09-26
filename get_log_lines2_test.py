import os
import sys
import pytest
from datetime import datetime
from get_log_lines2 import FileLocation

    
   
    
def test_path():
    expected = (
        r'C:\Users\megrust\Desktop\Workstuff\OCLC Datasync\Xrefs-20250519-e8w'
        )
    assert FileLocation().pathname == expected
    
def get_c_date():
    expected = (
        '20250519'
        )
    assert FileLocation().getcdate == expected
    
#@pytest.mark.skip    
def test_filename():
    expected = (
        '1012672.e8w.bib_20250519_040511.mrc'
        )
    assert FileLocation().mrc_file_name == expected
    
    
def test_get_date():
    expected = (
        '20250519'
        )
    assert FileLocation().input_date == expected
        
        
def test_get_libname():
    expected = (
        'e8w'
        )
    assert FileLocation().libcode == expected
    
    
def test_get_the_gd_file():
    expected = (
        'e8w-bib-20250519-keys.txt'
        )
    assert FileLocation().keyfilename == expected
    
    
def test_xreffilename():
    expected = (
        'E8W-E8W.1012672.IN.BIB.D20250519.T081003757.1012672.e8w.bib_20250519_040511.mrc.BibCrossRefReport.txt'
        )
    assert FileLocation().xreffilename == expected    
    
      
def test_key_count():
    expected = (
        379
        )
    assert FileLocation().keycount == expected
    
    
def test_xref_count():
    expected = (
        379
        )
    assert FileLocation().xrefcount == expected
    
    
def test_result_data():
    expected = (
        '1012672.e8w.bib_20250519_040511.mrc\te8w\tbib\t379\t20250519\t20250519\t20250519\t379\t0\t20250519\t293\t86\t0\t0'
        )
    assert FileLocation().reportresult() == expected
    
    
def test_key_create_date():
    expected = (
        '20250519'
        )
    assert FileLocation().key_create_date == expected
    
    
def test_xref_create_date():
    expected = (
        '20250519'
        )
    assert FileLocation().xref_create_date == expected
    
    
def test_report_create_date():
    expected = (
        '20250519'
        )
    assert FileLocation().report_create_date == expected
    

def test_report_data():
    expected = (
        '293\t86\t0\t0'
        )
    assert FileLocation().report_data == expected
    
   
def test_number_not_returned():
    expected = (
        0
        )
    assert FileLocation().number_not_returned == expected

 