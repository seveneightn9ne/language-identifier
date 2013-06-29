class Language(object):
    def __init__(self, name, passing_answers):
        """
        name is the name of the language e.g. 'javascript'
        passing_answers is a dict mapping questions to valid answers
            mapping answers to sets of valid answers is also ok.
            e.g. {
                question1: 'yes',
                question2: set('foo', 'bar'),
            }
        """
        self.name = name

        def format_answers(answers):
            if isinstance(answers, set) or isinstance(answers, list):
                return set(answers)
            else:
                return set([answers])
        self.passing_answers = map(format_answers, passing_answers)

    def check(self, question, answer_symbol):
        """
        Return whether the language is compatible with the question answer combination.
        """
        if question in self.passing_answers:
            if self.passing_answers[question] == answer_symbol:
                return True
            return False
        else:
            return True
