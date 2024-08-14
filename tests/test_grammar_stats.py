import pytest
from lib.grammar_stats import *

'''
EDGE CASE 
ARG : empty text
RETURN : raises error
'''
def test_check_empty_text():

    with pytest.raises(Exception) as err:
        grammar = GrammarStats()
        grammar.check("")
    assert str(err.value) == "Text must have content, please enter"



'''
ARG : text beginning capital letter  
RETURN : True
'''
def test_check_begins_with_capital_letter():
    grammar = GrammarStats()
    grammar.check("Love is a beautiful thing")
    assert True



'''
ARG : text beginning with lowercase letter
RETURN : False
'''
def test_check_begins_with_lowercase_letter():
    grammar = GrammarStats()
    result = grammar.check("the ocean is blue")

    # ---- USE VARIABLE TO FIX ASSERTION ERROR WHEN USING BOOLEAN
    assert result == False

'''
ARG : text beginning capital letter + ends with correct puncation  
RETURN : True
'''
def test_check_begins_with_capital_letter_ends_good_punctuation():
    grammar = GrammarStats()
    grammar.check("Love is a beautiful thing!")
    assert True

'''
ARG : text beginning capital letter + ends with no punctuation  
RETURN : True
'''
def test_check_begins_with_capital_letter_ends_no_punctuation():
    grammar = GrammarStats()
    result = grammar.check("Love is a beautiful thing")
    assert result == False

'''
ARG : text beginning with a number
RETURN : False
'''
def test_check_with_number():
    grammar = GrammarStats()
    result = grammar.check("3627904")
    assert result == False


'''
ARG : text beginning with a special character
RETURN : False
'''
def test_check_beginning_with_special_character():
    grammar = GrammarStats()
    result = grammar.check("!bhf")
    assert result == False



'''
--------------------------------------------------------------------------------------------
ARG : count number of texts in check(text) equating to True
RETURN : return int as a percentage
'''