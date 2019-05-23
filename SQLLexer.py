# -*- coding: utf-8 -*-  

import re
import ply.lex as lex

class SQLLexer(object):
    # reserved words
    reserved = {
        # data types
        'char': 'CHAR',
        'int': 'INT',
        'varchar': 'VARCHAR',

        # values
        'all': 'ALL',
        'any': 'ANY',
        'null': 'NULL',

        # case operators
        'where': 'WHERE',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'is': 'IS',
        'in': 'IN',

        # other key words
        'as': 'AS',
        'on': 'ON',
        'asc': 'ASC',
        'by': 'BY',
        'check': 'CHECK',
        'constraint': 'CONSTRAINT',
        'create': 'CREATE',
        'database': 'DATABASE',
        'databases': 'DATABASES',
        'delete': 'DELETE',
        'drop': 'DROP',
        'exit': 'EXIT',
        'foreign': 'FOREIGN',
        'from': 'FROM',
        'insert': 'INSERT',
        'into': 'INTO',
        'key': 'KEY',
        'order': 'ORDER',
        'primary': 'PRIMARY',
        'set': 'SET',
        'select': 'SELECT',
        'join': 'JOIN',
        'show': 'SHOW',
        'table': 'TABLE',
        'tables': 'TABLES',
        'union': 'UNION',
        'unique': 'UNIQUE',
        'update': 'UPDATE',
        'use': 'USE',
        'values': 'VALUES',
    }

    # List of token names.   This is always required
    tokens = [
        'NOTEQUALS',
        'NUMBER',
        'BOOLEAN',
        'ID',
        'STRING',
        'COMMENT',
             ] + list(reserved.values())

             # Literals.  Should be placed in module given to lex()
    # literals = ['+', '-', '*', '/', '>', '<', '=', '(', ')', ',', ';']
    literals = '+-*/<>()=,;'

    # Regular expression rules for simple tokens
    t_NOTEQUALS = '!='

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r"""'(.*?)'|\"(.*?)\""""
        t.value = t.value[1:-1]
        return t

    def t_BOOLEAN(self, t):
        r'[tT][rR][uU][eE]|[fF][aA][lL][sS][eE]'
        if 'true' == str.lower(t.value):
            t.value = True
        elif 'false' == str.lower(t.value):
            t.value = False
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(str.lower(t.value), 'ID')  # Check for reserved words
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'
    t_COMMENT = r'//.*'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        # set lex to be case-insensitive
        self.lexer = lex.lex(module=self, reflags=int(re.IGNORECASE | re.VERBOSE), **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)

if __name__ == "__main__":
    data = '''
    3 + 4
    selEct e,d fRom hello
    where 1=2 anD 255<3;
    'nihao'
    "jdsa d aow pap hfp"
    //comments
    '''
    data = '''
SELECT SNAME,SAGE FROM STUDENT JOIN TEACHER;
SELECT * FROM STUDENT;
SELECT SNAME,SAGE FROM STUDENT WHERE SAGE=21;
SELECT SNAME,SAGE FROM STUDENT WHERE (((SAGE=21)));
SELECT SNAME,SAGE FROM STUDENT WHERE (SAGE>21) AND (SSEX=0);
SELECT SNAME,SAGE FROM STUDENT WHERE (SAGE>21) OR (SSEX=0);
SELECT * FROM STUDENT WHERE SSEX!=1;
// 测试多表查询
SELECT * FROM STUDENT;SELECT * FROM COURSE;
select * from student,course;
SELECT * FROM STUDENT,COURSE WHERE (SSEX=0) AND (CID=1);
//测试DELETE语句
SELECT * FROM STUDENT;
DELETE FROM STUDENT WHERE (SAGE>21) AND (SSEX=0);
SELECT * FROM STUDENT;
//测试UPDATE
SELECT * FROM STUDENT;
UPDATE STUDENT SET SAGE=21 WHERE SSEX=1;
SELECT * FROM STUDENT;
UPDATE STUDENT SET SAGE=27,SSEX=1 WHERE SNAME='ZHANGSAN';
SELECT * FROM STUDENT;
    '''
    #data = 'true and false "sasas exit" Quit'
    #data = '1+2 true'

    # Build the lexer and try it out
    m = SQLLexer()
    m.build()        # Build the lexer
    m.test(data)     # Test it