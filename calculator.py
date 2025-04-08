class Calculator:
    def precedence(self, op):
        if op in ('+','-'):
            return 1
        if op in ('*','/'):
            return 2
        return 0
    
    def apply_op(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0: 
                raise ZeroDivisionError("Division by Zero")
            return a / b
    
    def evaluate (self, expression):
        try:
            values = []
            ops = []
            i=0
            while i < len(expression):
                if expression[i] == ' ':
                    i += 1
                    continue
                if expression[i] == '(':
                    ops.append(expression[i])
                elif expression[i].isdigit() or expression[i] == '.':
                    val = ''
                    while i < len (expression) and (expression[i].isdigit() or expression[i] == '.'):
                        val += expression[i]
                        i += 1
                    values.append(float(val))
                    i -= 1
                elif expression[i] == ')':
                    while ops and ops[-1] != '(':
                        b = values.pop()
                        a = values.pop()
                        op = ops.pop()
                        values.append(self.apply_op(a, b, op))
                    ops.pop()
                else:
                    while ops and self.precedence(ops[-1]) >= self.precedence(expression[i]):
                        b = values.pop()
                        a = values.pop()
                        op = ops.pop()
                        values.append(self.apply_op(a, b, op))
                    ops.append(expression[i])
                i += 1

            while ops:
                b = values.pop()
                a = values.pop()
                op = ops.pop()
                values.append(self.apply_op(a, b, op))

            return str(values[0])
        except Exception:
            return "Error"

        

    