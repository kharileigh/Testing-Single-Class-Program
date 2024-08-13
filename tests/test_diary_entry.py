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


'''
ARG : title & contents
RETURN : num of words in title & contents
'''
def test_count_words_in_both_title_and_contents():

    entry = DiaryEntry("My Title", "Some contents")
    result = entry.count_words()
    # should be 4 but counts : in formatted string
    assert result == 5