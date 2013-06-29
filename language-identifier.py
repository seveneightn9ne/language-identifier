from language import Language
from question import Question

def findin(f, l):
    """ Like filter() but short-circuiting and returns a boolean """
    for e in l:
        if f(e):
            return True
    return False


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
    parens = Question("Are there lots of parenthesis?", {
        'yes': "Yes.",
        'no' : "No.",
        })
    js = Language("javascript", {
        parens: 'yes' })
    lisp = Language("lisp", {
        parens: 'yes' })

    languages = set([js, lisp])
    questions = [parens]
    run_game(languages, questions)
