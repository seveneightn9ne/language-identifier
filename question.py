class Question(object):
    def __init__(self, question="", choices=None):
        self.question = question
        self.choices = choices or []

    def ask(self):
        print(self.question + "\n")
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
