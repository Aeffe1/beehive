import pytest
import pymarc
from slavic_extract import MarcRecords

    
def test_print_slavic_title():
    expected = (
        'Nevidljivi heroji Grčke'
        )
    assert MarcRecords('setout5.mrc').print_slavic_title() == expected
    
    
def test_all_titles_and_labels():
    expected = (
        'SYSNUM:99188878199206381'"\t"
        'FMT:BK'"\t"
        'LANG:   '"\t"
        'TITLE:Nevidljivi heroji Grčke'"\t"
        'AUTHOR:Blagojevic, Gordana'"\t"
        'AUTHOR_TAG:100'"\t"
        'DATE:2024'"\t"
        'TITLE_H:'"\t"
        'IMPRINT:Etnografski institut SANU,'"\t"
        'ARRIVAL_DATE:2025-03-25'"\t"
        'ISBN:9788675871262'
        )
    assert MarcRecords('setout5.mrc').all_titles_and_labels() == expected