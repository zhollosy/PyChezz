from pysideuic import compileUi

pyfile = open('x:\work\_DEV\QtTests\pyChezz\pyChezzUI.py', 'w')
compileUi('x:\work\_DEV\QtTests\pyChezz\pyChezzUI.ui', pyfile, False, 4, False)

pyfile.close()

