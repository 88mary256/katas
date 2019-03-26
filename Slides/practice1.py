a=13
b=2
print "El suma de a y b es: "+ str(a+b)
print a-b
print a*b
print a**b
print a/b
print a%b


print "Create a function that receive 3 arguments :"
print "2 numbers"
print "1 operations"

OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}

def apply_operator(a, op, b):

    method = '__%s__' % OPERATORS[op]
    print method
    return getattr(b, method)(a)

print apply_operator(5, "+", 2)
