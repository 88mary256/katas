import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "%": operator.mod, "/": operator.div,
       "**": operator.pow, "==": operator.eq, ">": operator.gt, "<": operator.lt, "<=": operator.le, ">=": operator.ge,
       "!=": operator.ne, "//": operator.floordiv}


def perform_operation(op, a, b):
    return ops[op](int(a), int(b))


def perform_and_print_operation(op, a, b):
    result = perform_operation(op, a, b)
    print "{} {} {} = {}".format(a, op, b, result)
    return result


c = perform_operation("*", "5", "6")
print c
perform_and_print_operation("*", "5", "6")
perform_and_print_operation("+", "2", "5")
perform_and_print_operation("-", "2", "5")
perform_and_print_operation("*", "2", "5")
perform_and_print_operation("/", "2", "5")
perform_and_print_operation("%", "2", "5")
perform_and_print_operation("/", "5", "2")
perform_and_print_operation("%", "5", "2")
perform_and_print_operation("//", "-11", "3")
perform_and_print_operation("//", "9", "2")
perform_and_print_operation("**", "5", "2")
perform_and_print_operation("==", "5", "2")
perform_and_print_operation("!=", "5", "2")
perform_and_print_operation("<", "5", "2")
perform_and_print_operation(">", "5", "2")
perform_and_print_operation("<=", "5", "2")
perform_and_print_operation(">=", "5", "2")


