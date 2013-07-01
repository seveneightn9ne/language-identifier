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
    full_parens = Question("Do parenthesis surround all calls\nLike this: (sum 4 (product 3 2))?", {
        'yes': "Yes.",
        'no':  "No.",
    })

    message_passing = Question("Are methods called via messages that look like this?\nexample: [[MyObject alloc] init]", {
        'yes': "Yes.",
        'no':  "No.",
    })

    pin_mode = Question("Is the pinMode(a,b) function called?", {
        'yes': "Yes.",
        'no':  "No.",
    })

    semicolons = Question("Do semicolons end most lines?", {
        'yes': "Yes.",
        'no': "No.",
    })

    variable_declaration = Question("What does it look like when a NEW variable is set?", {
        'type=': "int x = 4",
        'var=': "var x = 4",
        'val=': "val x = 4",
        '$=': "$foo = 4",
        'let': "let foo 4",
        'defn': "defn",
        'implicit': "x = 4",
    })

    languages = set([
        Language("C", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: ['type='],
        }),
        Language("C++", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: ['type='],
        }),
        Language("Objective-C", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes', 'no'],
            variable_declaration: ['type='],
        }),
        Language("Python", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['no'],
            variable_declaration: ['implicit'],
        }),
        Language("Javascript", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes', 'no'],
            variable_declaration: ['var='],
        }),
        Language("Coffeescript", {
            full_parens: ['yes', 'no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes', 'no'],
            variable_declaration: ['var='],
        }),
        Language("PHP", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: ['$='],
        }),
        Language("Perl", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: ['$='],
        }),
        Language("SQL", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: [],
        }),
        Language("Arduino", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['yes'],
            semicolons: ['yes'],
            variable_declaration: ['type='],
        }),
        Language("Java", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['yes'],
            variable_declaration: ['type='],
        }),
        Language("Lisp", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['no'],
            variable_declaration: ['let', 'defn'],
        }),
        Language("Scheme", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['no'],
            variable_declaration: ['let', 'defn'],
        }),
        # Language("R", {
        # }),
        Language("Brainf**k", {
            full_parens: ['no'],
            message_passing: ['no'],
            pin_mode: ['no'],
            semicolons: ['no'],
            variable_declaration: [],
        }),
    ])

    questions = set([full_parens, message_passing, pin_mode, semicolons, variable_declaration])

    return languages, questions
