def answer(question):
    operation = None
    number = None

    question = question.removeprefix("What is").removesuffix("?").strip()
    for word in question:
        if word.isdigit():
            number = int(word)
        elif word in ('plus','minus','multiplied by','divided by'):
            operation = word
        else:
            raise ValueError('syntax error')
        

    return answer

print(answer('What is 5 plus 13?'))