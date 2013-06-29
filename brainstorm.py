lispy_functions = YesNoQuestion(
    question="How do you define functions?",
    yes="(defn function foobar)"
    no="def function" )

variable_declaration = MultipleChoiceQuestion(
    question="How do you define a variable?"
    answers={
        'var'      : "var x = 'foo'"
        'val'      : "val x = 'foo'"
        'implicit' : "x = 'foo'"
    }
    )

lispy_functions = MultipleChoiceQuestion(
    question="How do you define functions?",
    answers={
        'yes'  :  "(defn function foobar)"
        'no' :  "def function"
    })


javascript = language(name="javascript"
                      answers={
                        lispy_functions: False
                      })


class YesNoQuestion(Question):
    def __init__(self, question, yes, no):
        self.question = question
        self.yes = yes
        self.no = no

    def ask():
        # stuff
        # print strings to user
        # return True or False
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, question, answers)


question = lispy_functions
answer = question.ask()
for language in languages:
    if isinstance(question, YesNoQuestion):
        if language.answers[question] == answer:
            language will stay in our pool
        else:
            kick it out
    elif isinstance(question, MultipleChoiceQuestion):
        # do other stuff
