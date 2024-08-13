import pytest
from lib.diary_entry import *

'''
EDGE CASE 
ARG : empty title & contents 
RETURN : raises error
'''
def test_empty_title_and_contents():

    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "Diary entries must have titles and contents"

'''
ARG : title & contents
RETURN : formatted entry
'''
def test_format_with_title_and_contents_given():
    entry = DiaryEntry("My Title", "Some contents")
    result = entry.format()
    assert result == "My Title : Some contents"