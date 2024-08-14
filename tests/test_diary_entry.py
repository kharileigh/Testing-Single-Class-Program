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
------------------------------------------------------------------------------------------
ARG : title & contents
RETURN : num of words in title & contents
'''
# ------ ASSERTION SHOULD BE: 4
def test_count_words_in_both_title_and_contents():

    entry = DiaryEntry("My Title", "Some contents")
    result = entry.count_words()
    # should be 4 but counts : in formatted string
    assert result == 5


'''
------------------------------------------------------------------------------------------
ARG : wpm = 2, text = 2 words
RETURN : 1 minute
'''
def test_reading_time_with_two_wpm_and_two_words():
    
    entry = DiaryEntry("My Title", "Some contents")
    result = entry.reading_time(2)
    assert result == 1


'''
ARG : wpm = 2, text = 4 words
RETURN : 2 mins
'''
def test_reading_time_with_two_wpm_and_four_words():

    entry = DiaryEntry("My Title", "one two three four")
    result = entry.reading_time(2)
    assert result == 2


'''
ARG : wpm = 2, text = 3 words
RETURN : 2 mins (round UP - ceil)
'''
def test_reading_time_with_two_wpm_and_three_words():

    entry = DiaryEntry("My Title", "one two three ")
    result = entry.reading_time(2)
    assert result == 2


'''
ARG : wpm = 0
RETURN : raises error
'''
def test_reading_time_wpm_of_zero():

    entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err:
        entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time"



'''
------------------------------------------------------------------------------------------
ARG : contents = 6 words, wpm = 2, minutes = 1
RETURN : first 2 words
'''
# ------ ASSERTION SHOULD BE: "one two"
def test_reading_chunk_with_two_wpm_and_one_minute():
    entry = DiaryEntry("My Title", "one two three four five six")
    result = entry.reading_chunk(2, 1)
    assert result == "one two"



'''
ARG : contents = 6 words, wpm = 2, minutes = 2
RETURN : first 4 words
'''
def test_reading_chunk_with_two_wpm_and_two_minutes():
    entry = DiaryEntry("My Title", "one two three four five six")
    result = entry.reading_chunk(2, 2)
    assert result == "one two three four"
    


'''
ARG : contents = 6 words, wpm = 2, minutes = 1
1st FUNCTION CALL RETURNS "one two"
2nd FUNCTION CALL RETURNS "three four"
3rd FUNCTION CALL RETURNS "five six"
'''
def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    entry = DiaryEntry("My Title", "one two three four five six")
    assert entry.reading_chunk(2, 1) == "one two"
    assert entry.reading_chunk(2, 1) == "three four"
    assert entry.reading_chunk(2, 1) == "five six"



'''
ARG : 6 words
FUNCTION CALLED REPEATEDLY
LAST CHUNK = last words in text, even shorted than words user can read
LAST FUNCTION CALL = restart from beginning
'''
def test_reading_chunk_wraps_around_on_multiple_calls():
    entry = DiaryEntry("My Title", "one two three four five six")
    assert entry.reading_chunk(2, 2) == "one two three four"
    assert entry.reading_chunk(2, 2) == "five six"
    assert entry.reading_chunk(2, 2) == "one two three four"



'''
ARG : 6 words
FUNCTION CALLED REPEATEDLY -- WITH AN EXACT ENDING
LAST CHUNK = LAST WORDS IN TEXT
NEXT CALL = START FROM BEGINNING
'''
def test_reading_chunk_wraps_around_on_multiple_calls_exact_ending():
    entry = DiaryEntry("My Title", "one two three four five six")
    assert entry.reading_chunk(2, 2) == "one two three four"
    assert entry.reading_chunk(2, 1) == "five six"
    assert entry.reading_chunk(2, 2) == "one two three four"



