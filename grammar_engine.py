def check_sentence(sentence, dictionary):

    errors = []

    words = sentence.lower().replace(".","").replace("?","").split()

    pos_tags = []

    for w in words:

        if w not in dictionary:
            errors.append(f"Unknown word: {w}")
        else:
            pos_tags.append(dictionary[w])

    # RULE 1 repeated word
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            errors.append("Repeated word detected")

    # RULE 2 sentence start capital
    if sentence[0].islower():
        errors.append("Sentence should start with capital letter")

    # RULE 3 punctuation
    if sentence[-1] not in ".?!":
        errors.append("Sentence should end with punctuation")

    # RULE 4 missing verb
    if "verb" not in pos_tags:
        errors.append("Sentence may be missing a verb")

    # RULE 5 noun noun noun
    if "noun noun noun" in " ".join(pos_tags):
        errors.append("Unusual noun sequence")

    # RULE 6 verb start
    if pos_tags and pos_tags[0] == "verb":
        errors.append("Sentence begins with verb")

    # RULE 7 two verbs
    for i in range(len(pos_tags)-1):
        if pos_tags[i]=="verb" and pos_tags[i+1]=="verb":
            errors.append("Two verbs together")

    # RULE 8 two pronouns
    for i in range(len(pos_tags)-1):
        if pos_tags[i]=="pronoun" and pos_tags[i+1]=="pronoun":
            errors.append("Two pronouns together")

    # RULE 9 determiner determiner
    for i in range(len(pos_tags)-1):
        if pos_tags[i]=="determiner" and pos_tags[i+1]=="determiner":
            errors.append("Repeated determiners")

    # RULE 10 preposition end
    if pos_tags and pos_tags[-1]=="preposition":
        errors.append("Sentence ends with preposition")

    # RULE 11 conjunction start
    if pos_tags and pos_tags[0]=="conjunction":
        errors.append("Sentence starts with conjunction")

    # RULE 12 adjective verb
    if "adjective verb" in " ".join(pos_tags):
        errors.append("Adjective before verb")

    # RULE 13 noun adjective adjective
    if "noun adjective adjective" in " ".join(pos_tags):
        errors.append("Too many adjectives")

    # RULE 14 adverb noun
    if "adverb noun" in " ".join(pos_tags):
        errors.append("Adverb before noun")

    # RULE 15 noun verb verb
    if "noun verb verb" in " ".join(pos_tags):
        errors.append("Double verbs after noun")

    # RULE 16 pronoun noun
    if "pronoun noun" in " ".join(pos_tags):
        errors.append("Pronoun before noun unusual")

    # RULE 17 adjective adjective noun
    if "adjective adjective noun" in " ".join(pos_tags):
        errors.append("Too many adjectives before noun")

    # RULE 18 noun preposition noun
    if "noun preposition noun" in " ".join(pos_tags):
        pass

    # RULE 19 noun verb adjective
    if "noun verb adjective" in " ".join(pos_tags):
        pass

    # RULE 20 verb noun verb
    if "verb noun verb" in " ".join(pos_tags):
        errors.append("Unusual verb pattern")

    return errors