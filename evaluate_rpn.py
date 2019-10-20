def evaluate_rpn(expression: str):
    intermediate_result = []
    delimiter = ','
    operators = {'+': lambda x, y : x + y,
                 ' -': lambda x, y : x -y,
                 'x': lambda x, y : x * y,
                 '/' : lambda y, x : x // y
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_result.append(operators[token](
                intermediate_result.pop(),intermediate_result.pop()
            ))
        else:
            intermediate_result.append(int(token))
    return intermediate_result[-1]



print(evaluate_rpn("3,4,+,2,x,1,+"))

