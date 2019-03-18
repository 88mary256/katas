

print "Create a function that receive 3 arguments :"
print "2 numbers"
print "1 operations"
'''
def perform_operation(operator, num1, num2):
    r = num1+operator+num2

    eval(r)



    print r
perform_operation("+", "2", "3")
'''
OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}

def apply_operator(a, op, b):

    method = '__%s__' % OPERATORS[op]
    print method
    return getattr(b, method)(a)

print apply_operator(5, "+", 2)