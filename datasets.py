"""
dataset functions return tuples of (languages, questions)
where languages and questions are sets
"""

from language import Language
from question import Question


def simpleset():
    parens = Question("Are there lots of parenthesis?", {
        'yes': "Yes.",
        'no':  "No.",
    })

    js = Language("Javascript", {
        parens: ['no']
    })

    lisp = Language("Lisp", {
        parens: ['yes']
    })

    languages = set([js, lisp])
    questions = [parens]

    return languages, questions


def biggerset():
    parens = Question("Are there lots of parenthesis?", {
        'yes': "Yes.",
        'no':  "No.",
    })

    intuitive = Question("Do you have idea what it's doing?", {
        'yes': "Yes.",
        'no':  "No.",
    })

    js = Language("Javascript", {
        parens: ['yes'],
        intuitive: ['yes'],
    })

    lisp = Language("Lisp", {
        parens: ['yes'],
        intuitive: ['yes'],
    })

    brainfuck = Language("Brainf**k", {
        parens: ['no'],
        intuitive: ['no'],
    })

    languages = set([js, lisp, brainfuck])
    questions = [parens, intuitive]

    return languages, questions
