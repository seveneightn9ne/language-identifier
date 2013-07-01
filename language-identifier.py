def filter_with_question(question, possible_languages):
    answer = question.ask()
    return set(filter(lambda x: x.check(question, answer), possible_languages))


def pick_next_question(unasked_questions, possible_languages):
    question_ranks = {}
    for question in unasked_questions:
        number_choices = len(question.choices)
        choice_ranks = {choice: 0 for choice in question.choices}
        for language in possible_languages:
            for choice in language.passing_answers[question]:
                choice_ranks[choice] += 1
        choice_ranks_list = [(choice, choice_ranks[choice]) for choice in choice_ranks if choice_ranks[choice] != 0]
        choice_ranks_list = sorted(choice_ranks_list, key=lambda (choice, rank): rank)
        if len(choice_ranks_list) <= 1:
            question_ranks[question] = 999
        else:
            question_ranks[question] = abs(choice_ranks_list[0][1]-choice_ranks_list[-1][1])
    return min(question_ranks.iterkeys(), key=lambda k: question_ranks[k])


def run_game(all_languages, all_questions):
    unasked_questions = list(all_questions)
    possible_languages = set(all_languages)

    while len(possible_languages) > 1:
        if len(unasked_questions) == 0:
            print "I don't know this language. (out of questions)"
            return None

        # TODO pick next question in an aware way
        question = pick_next_question(unasked_questions, possible_languages)
        unasked_questions.remove(question)
        possible_languages = filter_with_question(question, possible_languages)

    if len(possible_languages) is 0:
        print "I don't know this language. (no matching languages)"
        return None

    selected_langauge = possible_languages.pop()
    print "You're looking at {}.".format(selected_langauge.name)
    return selected_langauge


if __name__ == "__main__":
    import datasets
    print "Welcome to the programming language identifier!"
    while True:
        print "What would you like to do?"
        print "1. (i)dentify a language"
        print "2. (l)earn about a language"
        print "3. (a)dd a language or question"
        print "4. Run the analy(z)er"
        print "5. (q)uit"
        action = raw_input("> ").strip()
        if action == "1" or action == "i":
            run_game(*datasets.picky_dataset())
        if action == "5" or action == "q":
            break
