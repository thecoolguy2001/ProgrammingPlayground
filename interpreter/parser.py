import ply.yacc as yacc
from .tokens import tokens

class NumberNode:
    def __init__(self, value):
        self.value = value

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class VarNode:
    def __init__(self, name):
        self.name = name

class AssignNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class IfNode:
    def __init__(self, cond, then_expr, else_expr):
        self.cond = cond
        self.then_expr = then_expr
        self.else_expr = else_expr

def p_program(p):
    '''program : expression'''
    p[0] = p[1]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = NumberNode(p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinOpNode(p[1], p[2], p[3])

def p_expression_var(p):
    '''expression : ID'''
    p[0] = VarNode(p[1])

def p_expression_assign(p):
    '''expression : ID EQUALS expression'''
    p[0] = AssignNode(p[1], p[3])

def p_expression_if(p):
    '''expression : IF expression LBRACE expression RBRACE ELSE LBRACE expression RBRACE'''
    p[0] = IfNode(p[2], p[4], p[8])

def p_error(p):
    raise Exception("Syntax error in input!")

parser = yacc.yacc()
