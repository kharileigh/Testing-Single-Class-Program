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