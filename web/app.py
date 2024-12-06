from flask import Flask, request, jsonify, render_template
import sys
  # Ensure we can import from parent directory if needed

from interpreter.tokens import lexer
from interpreter.parser import parser
from interpreter.evaluator import evaluate, Environment


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form.get('code', '')
    try:
        lexer.input(code)
        ast = parser.parse(code, lexer=lexer)
        env = Environment()
        result = evaluate(ast, env)
        return jsonify({"result": result, "error": None})
    except Exception as e:
        return jsonify({"result": None, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
