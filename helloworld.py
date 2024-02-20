from Interpreter import MyPythonInterpreter


mypython_code = """write ( "Hello, World!" ) """

interpreter = MyPythonInterpreter()
interpreter.interpret(mypython_code)
