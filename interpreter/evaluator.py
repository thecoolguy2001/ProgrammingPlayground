from .parser import NumberNode, BinOpNode, VarNode, AssignNode, IfNode

class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent is not None:
            return self.parent.get(name)
        else:
            raise Exception(f"Variable '{name}' not defined.")

    def set(self, name, value):
        self.vars[name] = value

def evaluate(node, env=None):
    if env is None:
        env = Environment()

    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, VarNode):
        return env.get(node.name)
    elif isinstance(node, BinOpNode):
        left_val = evaluate(node.left, env)
        right_val = evaluate(node.right, env)
        if node.op == '+':
            return left_val + right_val
        elif node.op == '-':
            return left_val - right_val
        elif node.op == '*':
            return left_val * right_val
        elif node.op == '/':
            if right_val == 0:
                raise Exception("Division by zero!")
            return left_val / right_val
    elif isinstance(node, AssignNode):
        val = evaluate(node.expr, env)
        env.set(node.name, val)
        return val
    elif isinstance(node, IfNode):
        cond_val = evaluate(node.cond, env)
        if cond_val:
            return evaluate(node.then_expr, env)
        else:
            return evaluate(node.else_expr, env)
    else:
        raise Exception("Unknown node type")
