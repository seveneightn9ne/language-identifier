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
            print "I don't know this language. (out of questions)"
            return None

        # TODO pick next question in an aware way
        question = unasked_questions.pop()
        possible_languages = filter_with_question(question, possible_languages)

    if len(possible_languages) is 0:
        print "I don't know this language. (no matching languages)"
        return None

    selected_langauge = possible_languages.pop()
    print "Your looking at {}.".format(selected_langauge.name)
    return selected_langauge


if __name__ == "__main__":
    parens = Question("Are there lots of parenthesis?", {
        'yes': "Yes.",
        'no' : "No.",
        })

    js = Language("javascript", {
        parens: ['no'] })

    lisp = Language("lisp", {
        parens: ['yes'] })

    languages = set([js, lisp])
    questions = [parens]

    run_game(languages, questions)

    # print lisp.check(parens, 'no')
