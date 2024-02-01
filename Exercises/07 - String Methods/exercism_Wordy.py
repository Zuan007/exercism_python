def answer(question):
    operation = None
    number = None

    for word in question:
        if word.isdigit():
            number = int(word)
        elif word in ('plus','minus','multiplied','divided'):
            operation = word
        elif word == 'is':
            continue
        else:
            raise ValueError('syntax error')
        
    if operation == 'plus':
        answer += number
    if operation == 'minus':
        answer -= number
    if operation == 'multiplied':
        answer *= number
    if operation == 'divided':
        answer /= number

    return answer

problem_2 = "What is 5 plus 13?"
print(answer(problem_2))