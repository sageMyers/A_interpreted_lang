from Interpreter import MyPythonInterpreter


mypython_code = """write ( "Hello,MyPython!" ) """

interpreter = MyPythonInterpreter()
interpreter.interpret(mypython_code)