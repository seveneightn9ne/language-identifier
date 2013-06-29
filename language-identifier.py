
class Question(object):
    def __init__(question="", choices=None):
        self.question = question
        self.choices = choices or []

    def ask():
        print(question + "\n")
        for i, choice in enumerate(choices): print(choice)
        def _ask():
            try:
                answer = int(raw_input(question))
            except ValueError:
                print("Not a valid number")
                return _ask()
            if choices.size() < answer+1:
                print("Not a valid number")
                return _ask()
            return answer

        return _ask()

    # def analyze_answer():


class Language(object):
    def __init__(name="", answers=None):
        self.name = name
        self.answers = answers

    def response_to(self, question):
        if answers.contains(question): return self.answers[question]
        return None

    def add_answer(self, question, answer):
        pass

questions = [Question("How do you define a function?",
                        ["def foo(bar, baz): ...", 
                         "function foo(bar, baz) { ... }", 
                         "There are no functions in this language",
                         "I don't know / other"]
                     )]
possible_languages = [Language("Python", {questions[0]: 0}), Language("JavaScript")]

for question in questions:
    answer = question.ask()
    for language in possible_languages:
        if language.response_to(question) != answer:
            possible_languages.remove(language)
    if possible_languages.size() == 1:
        print "The language is "+possible_languages[0].name
        break
    if possible_languages.size() == 0:
        print "I don't know this language."
        break