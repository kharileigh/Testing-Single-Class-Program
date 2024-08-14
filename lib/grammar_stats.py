class GrammarStats():

    # ------ ADD COUNTER TO CONSTRUCTOR
    # ------ count increases in check
    # ------ compares counts in percentage check
    def __init__(self):
        
        self.total_texts = 0
        self.good_grammar_texts = 0



    def check(self, text):

        punctuation = ".!?"

        if text == "":
            raise Exception("Text must have content, please enter")
        
        #---- increase total counter if string is not empty
        self.total_texts += 1

        if text[0].isupper() and text[-1] in punctuation:

            #----- increase good grammar counter if True
            self.good_grammar_texts += 1
            return True
        
        return False



    def percentage_good(self):
        
        return int((self.good_grammar_texts / self.total_texts) * 100)