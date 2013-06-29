
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



def filter_with_question(question, possible_languages):
    answer = question.ask()
    return set(filter(lambda x: x.check(question, answer), possible_languages))


def run_game(all_languages, all_questions):
    unasked_questions = list(all_questions)
    possible_languages = set(all_languages)

    while len(possible_languages) > 1:
        if len(unasked_questions) == 0:
            print "I don't know this language."
            return None

        question = unasked_questions.pop()
        possible_languages = filter_with_question(question, possible_languages)

    selected_langauge = possible_languages.pop()
    print "Your looking at {}.".format(selected_langauge.name)
    return possible_languages.pop()


if __name__ == "__main__":
    run_game()
