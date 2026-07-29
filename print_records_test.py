import pytest
import pymarc
from print_records import MarcPrint

#python -m pytest print_records_test.py -vv

        
def test_get_ttl():
    expected = (
        'AA book projects review '
        )
    assert MarcPrint('test_one.mrc').ttl == expected

def test_get_reckey():
    expected = (
        '990056150940106381'
        )
    assert MarcPrint('test_one.mrc').reckey == expected
    
def test_get_issns():
    expected = (
        '20524757|25034499'
        )
    assert MarcPrint('test_one.mrc').issns == expected
    
def test_get_subjects():
    expected = (
        'Fashion Periodicals http id loc gov authorities subjects sh2008103595|Architectural Association Great Britain School of Architecture Students Exhibitions Periodicals '
        )
    assert MarcPrint('test_one.mrc').subjects == expected
    
def test_results():
    expected = (
    '990056150940106381'"\t"
    '20524757|25034499'"\t"
    'AA book projects review '"\t"
    'Fashion Periodicals http id loc gov authorities subjects sh2008103595|Architectural Association Great Britain School of Architecture Students Exhibitions Periodicals '
    )
    assert MarcPrint('test_one.mrc').results == expected
    


