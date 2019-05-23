# -*- coding: utf-8 -*-  

from Queue import Queue
from prettytable import PrettyTable
from ExprNode import *
import os

class Functions(object):

    using_tables = []
    table_cache = []
    current_column = [[], []]

    def __init__(self):
        os.chdir("/home/huang/Documents/SoftwareModeling/Assignment9/DBMS")
        self.dbms_file = "db.info"
        self.table_file = "table.info"
        self.dbinfo = open(self.dbms_file, mode='r+')
        self.currentdb = None

    def __del__(self):
        self.dbinfo.close()

    def db_exists(self, name):
        name += '\n'
        self.dbinfo.seek(0,0)
        for line in self.dbinfo.readlines():
            if line == name:
                return True
        return False

    @staticmethod
    def del_db(file, db_name):
        db_name += '\n'
        with open(file, mode='r') as o_f:
            with open(file+'.tmp', mode='w') as n_f:
                # assign no return, fxxk python
                line = o_f.readline()
                while line:
                    if line == db_name:
                        pass
                    else:
                        n_f.write(line)
                    line = o_f.readline()
        os.remove(file)
        os.rename(file+'.tmp', file)

    @staticmethod
    def del_table(file, tbl_name):
        with open(file, mode='r') as o_f:
            with open(file+'.tmp', mode='w') as n_f:
                line = o_f.readline()
                while line:
                    if line.split('|')[0] == tbl_name:
                        pass
                    else:
                        n_f.write(line)
                    line = o_f.readline()
        os.remove(file)
        os.rename(file+'.tmp', file)

    @staticmethod
    def rm_dir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.removedirs(path)

    # db operate functions

    def use_database(self, db_name):
        if self.db_exists(db_name):
            self.currentdb = db_name
            print "Database changed to '%s'." % db_name
        else:
            raise Exception("SQLError: database '%s' doesn't exist!" % db_name)

    def create_database(self, db_name):
        if not self.db_exists(db_name):
            os.mkdir(db_name)
            open(db_name+"/table.info", mode="w").close()
            self.dbinfo.write(db_name+'\n')
            self.dbinfo.flush()
            print "Successfully created database '%s'!" % db_name
        else:
            raise Exception("SQLError: database '%s' already exists!" % db_name)

    def drop_database(self, db_name):
        if self.db_exists(db_name):
            self.rm_dir(db_name)
            self.dbinfo.close()
            self.del_db(self.dbms_file, db_name)
            self.dbinfo = open(self.dbms_file, mode='r+')
            print "Successfully dropped database '%s'!" % db_name
        else:
            raise Exception("SQLError: database '%s' doesn't exist!" % db_name)

    def show_databases(self):
        self.dbinfo.seek(0,0)
        dbs = self.dbinfo.readlines()
        x = PrettyTable(["database"])
        for db in dbs:
            x.add_row([db[:-1]])
        print x
        print "Query OK! %d row(s) matched." % len(dbs)

    def table_exists(self, tbl_name):
        if self.currentdb:
            with open(self.currentdb+'/'+self.table_file, 'r') as tbl_info:
                line = tbl_info.readline()
                while line:
                    if tbl_name == line.split('|')[0]:
                        return True
                    line = tbl_info.readline()
                return False
        else:
            raise Exception("SQLError: No database selected!")

    def show_tables(self):
        if self.currentdb:
            with open(self.currentdb+'/'+self.table_file, 'r') as tbl_info:
                tbls = tbl_info.readlines()
                x = PrettyTable(["table"])
                for tbl in tbls:
                    x.add_row([tbl.split('|')[0]])
                print x
                print "Query OK! %d row(s) matched." % len(tbls)
        else:
            raise Exception("SQLError: No database selected!")       

    def create_table(self, tbl_name, fields):
        if self.currentdb:
            if not self.table_exists(tbl_name):
                info = "%s" % tbl_name
                for item in fields:
                    info += '|%s %s'%(item[0], item[1])
                    if len(item) == 3:
                        info += ' '+str(item[2])
                info += '\n'
                with open(self.currentdb+"/"+self.table_file, 'r+') as table_info:
                    table_info.seek(0, 2)
                    table_info.write(info)
                open(self.currentdb + '/' + tbl_name + '.txt', mode='w').close()
                print("Successfully created table '%s'." % tbl_name)
            else:
                raise Exception("SQLError: table '%s' already exists!" % tbl_name)
        else:
            raise Exception("SQLError: No database selected!")

    def get_column_info(self, tbl_name):
        if self.currentdb:
            column_names, column_types = [], []
            with open(self.currentdb + '/' + self.table_file, 'r') as tbl_info:
                for line in tbl_info.readlines():
                    line = line[:-1]
                    if line.split('|')[0] == tbl_name:
                        column_types = line.split('|')[1:]
            for c in column_types:
                column_names.append(c.split()[0])
            return column_names, column_types
        else:
            raise Exception("SQLError: No database selected!")

    def insert_table(self, tbl_name, param):
        if self.currentdb:
            if self.table_exists(tbl_name):
                column_names, column_values = param[0], param[1]
                all_columns, all_column_names = [], []
                with open(self.currentdb + '/' + self.table_file, 'r+') as tbl_info:
                    for line in tbl_info.readlines():
                        line = line[:-1]
                        if line.split('|')[0] == tbl_name:
                            all_columns = line.split('|')[1:]

                for c in all_columns:
                    all_column_names.append(c.split()[0])

                if column_names:
                    for c in column_names:
                        if c not in all_column_names:
                            raise Exception("SQLError: no column named '%s'!" % c)
                    info = []
                    for c in all_column_names:
                        if c in column_names:
                            info.append(column_values[column_names.index(c)])
                        else:
                            info.append('')      
                else:
                    if len(all_columns) != len(column_values):
                        raise Exception("SQLError: wrong count of values!")
                    info = column_values
                with open(self.currentdb + '/' + tbl_name + '.txt', 'r+') as table_file:
                    table_file.seek(0,2)
                    info_str = reduce(lambda s1, s2: str(s1) + str(s2) + '|', info, '')
                    table_file.write(info_str + '\n')
                    print("Query OK! 1 row affected.")
            else:
                raise Exception("SQLError: table '%s' doesn't exist!" % tbl_name)
        else:
            raise Exception("SQLError: No database selected!")

    def drop_table(self, tbl_name):
        if self.currentdb:
            if self.table_exists(tbl_name):
                os.remove(self.currentdb + '/' + tbl_name + '.txt')
                self.del_table(self.currentdb + '/' + self.table_file, tbl_name)
                print "Successfully dropped table '%s'!" % tbl_name
            else:
                raise Exception("SQLError: table '%s' doesn't exist!" % tbl_name)
        else:
            raise Exception("SQLError: No database selected!")

    def del_table_cache(self):
        self.using_tables = []
        self.table_cache = []
        self.current_column = [[], []]

    def cache_tables(self):
        if self.using_tables and self.currentdb:
            for table in self.using_tables:
                column_names, _ = self.get_column_info(table)
                table_content = []
                with open(self.currentdb + "/" + table + '.txt', 'r') as tbl_file:
                    for line in tbl_file.readlines():
                        table_content.append(line.split('|')[:-1])
                self.table_cache.append([column_names, table_content])

    @staticmethod
    def product(a,b):
        return map(lambda i: map(lambda j: i+j, b), a)
        
    def select_table(self, table, condition):
        if self.currentdb:
            for t in table[0]:
                if not self.table_exists(t): 
                    raise Exception("SQLError: table '%s' doesn't exist!" % t)
            self.using_tables = table[0]
            self.cache_tables()
            select_columns = table[1]
            pxx = self.table_cache[0][1]
            all_column_names = self.table_cache[0][0]
            result_set = []
            for each_table_cache in self.table_cache[1:]:
                if each_table_cache[1]:
                    pxx = self.product(pxx, each_table_cache[1])
                    all_column_names.extend(each_table_cache[0])
            self.current_column[0] = all_column_names
            for each in pxx:
                self.current_column[1] = each
                if self.compute(condition):
                    result_set.append(self.current_column[1])
            self.del_table_cache()
            if select_columns != '*':
                exclude_columns = filter(lambda c: \
                                    c not in select_columns, \
                                        all_column_names.copy())
                map(lambda c: \
                    map(lambda s: \
                        s.pop(all_column_names.index(c)), \
                            result_set), \
                                exclude_columns)
                
                map(lambda c: \
                    all_column_names.pop(c), \
                        exclude_columns)
            
            x = PrettyTable(all_column_names)
            for r in result_set:
                x.add_row(r)
            print x
            print "Query OK! %d row(s) matched." % len(result_set)
                
        else:
            raise Exception("SQLError: No database selected!")

    def update_table(self, table, condition):
        tbl_name = table[0]
        column_values = table[1]
        if self.currentdb:
            if self.table_exists(tbl_name):
                file = self.currentdb + '/' + tbl_name + '.txt'
                column_names, column_types = self.get_column_info(tbl_name)
                self.current_column[0] = column_names
                cnt = 0
                with open(file, mode='r') as o_f:
                    with open(file+'.tmp', mode='w') as n_f:
                        line = o_f.readline()
                        while line:
                            self.current_column[1] = line.split('|')[:-1]
                            if not self.compute(condition):
                                n_f.write(line)
                            else:
                                for column_value in column_values:
                                    index = self.current_column[0].index(column_value[0])
                                    self.current_column[1][index] = column_value[1]
                                new_line = reduce(lambda s1, s2: str(s1)+str(s2) + '|', self.current_column[1], '')
                                n_f.write(new_line+'\n')
                                cnt+=1
                            line = o_f.readline()
                os.remove(file)
                os.rename(file + '.tmp', file)
                print "Query OK! %d row(s) affected." % cnt
            else:
                raise Exception("SQLError: table '%s' doesn't exist!" % tbl_name)
        else:
            raise Exception("SQLError: No database selected!")

    def delete_from_table(self, tbl_name, condition):
        if self.currentdb:
            if self.table_exists(tbl_name):
                file = self.currentdb + '/' + tbl_name + '.txt'
                column_names, column_types = self.get_column_info(tbl_name)
                self.current_column[0] = column_names
                cnt = 0
                with open(file, mode='r') as o_f:
                    with open(file+'.tmp', mode='w') as n_f:
                        line = o_f.readline()
                        while line:
                            self.current_column[1] = line.split('|')[:-1]
                            if not self.compute(condition):
                                n_f.write(line)
                            else:
                                cnt+=1
                            line = o_f.readline()  
                os.remove(file)
                os.rename(file + '.tmp', file)
                print "Query OK! %d row(s) affected." % cnt                          
            else:
                raise Exception("SQLError: table '%s' doesn't exist!" % tbl_name)
        else:
            raise Exception("SQLError: No database selected!")

    def get_column_value(self, column_name):
        column_names = self.current_column[0]
        index = column_names.index(column_name)
        res = self.current_column[1][index]
        return res
    
    def compute(self, tree):
        res = None
        if isinstance(tree, SingleOp):
            if not isinstance(tree.op, ExprNode):
                op = tree.op
            else:
                op = self.compute(tree.op)

            if tree.op_type == 'arith_minus':
                res = -int(op)
            elif tree.op_type == 'logic_not':
                res = not bool(op)
            elif tree.op_type == 'variable':
                res = self.get_column_value(tree.op)
        elif isinstance(tree, BinaryOp):
            if not isinstance(tree.op1, ExprNode):
                op1 = tree.op1
            else:
                op1 = self.compute(tree.op1)

            if not isinstance(tree.op2, ExprNode):
                op2 = tree.op2
            else:
                op2 = self.compute(tree.op2)
            try:
                if tree.op_type == 'arith_+':
                    res = int(op1) + int(op2)
                elif tree.op_type == "arith_-":
                    res = int(op1) - int(op2)
                elif tree.op_type == "arith_*":
                    res = int(op1) * int(op2)
                elif tree.op_type == "arith_/":
                    res = int(op1) / int(op2)
                elif tree.op_type == "logic_and":
                    res = bool(op1) and bool(op2)
                elif tree.op_type == "logic_or":
                    res = bool(op1) or bool(op2)
                elif tree.op_type == "compare_>":
                    res = (int(op1) > int(op2))
                elif tree.op_type == "compare_<":
                    res = (int(op1) < int(op2))
                elif tree.op_type == "compare_=":
                    res = (str(op1) == str(op2))
                elif tree.op_type == "compare_!=":
                    res = (str(op1) != str(op2))
            except Exception as e:
                print(e)
                res = False
        else:
            res = True
        return res

class OperationQueue(Queue):
    Fun = Functions()
    
    def __init__(self):
        Queue.__init__(self)

    def pop_queue(self):
        while not self.empty():
            item = self.get()
            try:
                if item.op_type == "sql_use_database":
                    self.Fun.use_database(item.op)
                elif item.op_type == "sql_show_databases":
                    self.Fun.show_databases()
                elif item.op_type == "sql_create_database":
                    self.Fun.create_database(item.op)
                elif item.op_type == "sql_drop_database":
                    self.Fun.drop_database(item.op)
                elif item.op_type == "sql_show_tables":
                    self.Fun.show_tables()
                elif item.op_type == "sql_create_table":
                    self.Fun.create_table(item.op1, item.op2)
                elif item.op_type == "sql_insert_table":
                    self.Fun.insert_table(item.op1, item.op2)
                elif item.op_type == "sql_select_table":
                    self.Fun.select_table(item.op1, item.op2)
                elif item.op_type == "sql_update_table":
                    self.Fun.update_table(item.op1, item.op2)
                elif item.op_type == "sql_delete_from_table":
                    self.Fun.delete_from_table(item.op1, item.op2)
                elif item.op_type == "sql_drop_table":
                    self.Fun.drop_table(item.op)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    Fun = Functions()
    # Fun.create_database("test")

    Fun.use_database("test")
    dbs = ["aa", "bb", "cc", "dd", "ee"]
    for db in dbs:
        if not Fun.db_exists(db):
            Fun.create_database(db)
    Fun.show_databases()
    for db in dbs:
        if Fun.db_exists(db):
            Fun.drop_database(db)
            pass