class Question(object):
    def __init__(self, question="", choices=None):
        """
        question is question text e.g. "Are there parens?"

        choices is a dict e.g. {
            'yes': "Yes.",
            'no': "Yes.",
        }
        """
        self.question = question
        self.choices = choices or []

    def ask(self):
        print "\n{}".format(self.question)
        keys = self.choices.keys()
        for i, key in enumerate(keys):
            print "{}. {}".format(i + 1, self.choices[key])

        def _ask():
            try:
                answer_i = int(raw_input("> ")) - 1
            except ValueError:
                print("Not a valid number")
                return _ask()
            if len(keys) < answer_i + 1:
                print("Not a valid number")
                return _ask()
            return keys[answer_i]

        return _ask()
