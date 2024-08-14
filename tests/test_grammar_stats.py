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

'''
ARG : text beginning with lowercase letter
RETURN : True
'''

'''
ARG : text beginning with a number
RETURN : True
'''

'''
ARG : text beginning with a special character
RETURN : True
'''




'''
--------------------------------------------------------------------------------------------
ARG : count number of texts in check(text) equating to True
RETURN : return int as a percentage
'''