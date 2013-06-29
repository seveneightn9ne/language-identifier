class Question(object):
    def __init__(self, question="", choices=None):
        self.question = question
        self.choices = choices or []

    def ask(self):
        print(self.question + "\n")
        for i, choice in enumerate(self.choices): print "{}. {}".format(i+1, choice)

        def _ask():
            try:
                answer = int(raw_input("> "))-1
            except ValueError:
                print("Not a valid number")
                return _ask()
            if len(self.choices) < answer + 1:
                print("Not a valid number")
                return _ask()
            return answer

        return _ask()

    # def analyze_answer():