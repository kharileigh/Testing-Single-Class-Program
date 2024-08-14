class GrammarStats():

    def check(self, text):

        punctuation = ".!?"

        if text == "":
            raise Exception("Text must have content, please enter")
        
        if text[0].isupper() and text[-1] in punctuation:
            return True
        return False
