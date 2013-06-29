class Language(object):
    def __init__(self, name, passing_answers):
        """
        name is the name of the language e.g. 'javascript'

        passing_answers is a dict mapping questions to a set of valid answers
            mapping questions to lists of valid answers is also ok.
            e.g. {
                question1: set('yes'),
                question2: set('foo', 'bar'),
                question3: ['words', 'tokens'],
            }
        """
        self.name = name
        self.passing_answers = {key: set(passing_answers[key]) for key in passing_answers}

    def check(self, question, answer_symbol):
        """
        Return whether the language is compatible with the question answer combination.
        """
        if question in self.passing_answers:
            if answer_symbol in self.passing_answers[question]:
                return True
            return False
        else:
            return True
