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
    questions = set([parens])

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
    questions = set([parens, intuitive])

    return languages, questions

def picky_dataset():
    contains_a = Question("Does it contain an a?", {
        'yes': "Yes",
        'no': "No"
    })
    contains_b = Question("Does it contain a b?", {
        'yes': "Yes",
        'no': "No"
    })
    contains_c = Question("Does it contain a c?", {
        'yes': "Yes",
        'no': "No"
    })
    abracadabra = Language("banana", {
        contains_a: ['yes'],
        contains_b: ['yes'],
        contains_c: ['no']
        })
    apple = Language("apple", {
        contains_a: ['yes'],
        contains_b: ['no'],
        contains_c: ['no']
        })
    boca = Language("boca", {
        contains_a: ['yes'],
        contains_b: ['yes'],
        contains_c: ['yes']
        })

    languages = set([abracadabra, apple, boca])
    questions = set([contains_a, contains_b, contains_c])

    return languages, questions

def newset():
    languages = set([
        Language("C", {}),
        Language("C++", {}),
        Language("Objective-C", {}),
        Language("Python", {}),
        Language("Javascript", {}),
        Language("PHP", {}),
        Language("Perl", {}),
        Language("SQL", {}),
        Language("Arduino", {}),
        Language("Java", {}),
        Language("Lisp", {}),
        Language("Scheme", {}),
        Language("R", {}),
        Language("Brainf**k", {}),
    ])

    questions = set()

    return languages, questions
