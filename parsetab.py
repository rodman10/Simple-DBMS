
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDrightNOTleft=NOTEQUALSnonassoc><left+-left*/right-ALL AND ANY AS ASC BOOLEAN BY CHAR CHECK COMMENT CONSTRAINT CREATE DATABASE DATABASES DELETE DROP EXIT FOREIGN FROM ID IN INSERT INT INTO IS JOIN KEY NOT NOTEQUALS NULL NUMBER ON OR ORDER PRIMARY SELECT SET SHOW STRING TABLE TABLES UNION UNIQUE UPDATE USE VALUES VARCHAR WHEREexpression_set : expression_set expression_sql\n        |               expression_sql\n    expression_sql : expression_create_database\n        |               expression_show_database\n        |               expression_use_database\n        |               expression_exit\n        |               expression_comments\n        |               expression_show_tables\n        |               expression_create_table\n        |               expression_drop_table\n        |               expression_insert_table\n        |               expression_select_table\n        |               expression_update_table\n        |               expression_delete_from_table\n    expression_show_database : SHOW DATABASES ';'expression_create_database : CREATE DATABASE ID ';'expression_use_database : USE ID ';'expression_create_database : DROP DATABASE ID ';'expression_exit : EXIT\n        |                EXIT ';'\n    expression_show_tables : SHOW TABLES ';' expression_create_table : CREATE TABLE ID '(' table_fields_definition ')' ';'expression_insert_table : INSERT INTO ID '(' fields ')' VALUES '(' given_values ')' ';'\n        |                        INSERT INTO ID VALUES '(' given_values ')' ';'\n    expression_select_table : SELECT '*' FROM tables ';'\n        |                        SELECT fields FROM tables ';'\n        |                        SELECT '*' FROM tables WHERE expression_logic ';'\n        |                        SELECT fields FROM tables WHERE expression_logic ';'\n    expression_update_table : UPDATE ID SET column_values ';'\n        |                        UPDATE ID SET column_values WHERE expression_logic ';'\n    column_values : column_values ',' column_value\n        |              column_value\n    column_value : ID '=' NUMBER\n        |             ID '=' STRING\n    expression_delete_from_table : DELETE FROM ID ';'\n        |                             DELETE FROM ID WHERE expression_logic ';'\n    tables : tables JOIN ID ON ID\n        |       tables ',' ID\n        |       ID\n    fields : fields ',' ID\n        |       ID\n    given_values : given_values ',' given_value\n        |             given_value\n    given_value : NUMBER\n        |            STRING\n    expression_drop_table : DROP TABLE ID ';'table_fields_definition : table_fields_definition ',' table_field_definition\n        |                        table_field_definition\n    table_field_definition : ID CHAR '(' NUMBER ')'\n        |                       ID INT\n        |                       ID VARCHAR '(' NUMBER ')'\n    expression_comments : COMMENTexpression_logic : expression_logic AND expression_logic\n        |                 expression_logic OR  expression_logic\n    expression_logic : '(' expression_logic ')' expression_logic : NOT expression_logicexpression_logic : BOOLEAN\n        |                 expression_comp\n    expression_comp : expression_comp_member '>' expression_comp_member\n        |                expression_comp_member '<' expression_comp_member\n        |                expression_comp_member '=' expression_comp_member\n        |                expression_comp_member NOTEQUALS expression_comp_member\n    expression_comp_member : expression_arith\n        |                       variable\n        |                       STRING\n    expression_arith : expression_arith '+' expression_arith\n        |                 expression_arith '-' expression_arith\n        |                 expression_arith '*' expression_arith\n        |                 expression_arith '/' expression_arith\n    expression_arith : '(' expression_arith ')'  expression_arith : NUMBER\n        |                  variable\n    expression_arith : '-' expression_arithvariable : ID"
    
_lr_action_items = {'NOTEQUALS':([85,86,87,90,91,92,125,126,127,129,148,149,150,151,153,],[-71,116,-63,-65,-64,-74,-63,-64,-73,-72,-66,-68,-67,-69,-70,]),'USE':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[2,2,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'DROP':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[10,10,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'NUMBER':([67,71,73,74,81,82,88,89,94,113,114,116,117,118,119,120,121,122,123,128,135,139,140,158,],[85,85,85,101,85,112,85,85,85,85,85,85,85,85,85,85,85,85,85,85,101,159,160,101,]),'CHAR':([78,],[107,]),'ON':([96,],[131,]),'SELECT':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[6,6,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'COMMENT':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[15,15,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'INSERT':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[8,8,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'SET':([37,],[51,]),'VARCHAR':([78,],[106,]),')':([29,55,75,76,77,83,85,87,90,91,92,93,99,100,101,102,108,124,125,126,127,129,130,138,142,143,144,145,146,147,148,149,150,151,152,153,154,157,159,160,161,162,163,],[-41,-40,103,-48,104,-58,-71,-63,-65,-64,-74,-57,-45,-43,-44,134,-50,152,153,-72,-73,-72,-56,-47,-53,-54,-62,-61,-60,-59,-66,-68,-67,-69,-55,-70,153,-42,162,163,164,-51,-49,]),'(':([44,46,57,67,71,73,81,88,89,94,106,107,113,114,116,117,118,119,120,121,122,123,128,136,],[58,60,74,88,88,88,88,88,128,88,139,140,88,88,128,128,128,128,128,128,128,128,128,158,]),'CREATE':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[9,9,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'*':([6,85,87,91,92,125,126,127,129,148,149,150,151,153,154,],[28,-71,121,-72,-74,121,-72,121,-72,121,-68,121,-69,-70,121,]),'-':([67,71,73,81,85,87,88,89,91,92,94,113,114,116,117,118,119,120,121,122,123,125,126,127,128,129,148,149,150,151,153,154,],[89,89,89,89,-71,122,89,89,-72,-74,89,89,89,89,89,89,89,89,89,89,89,122,-72,-73,89,-72,-66,-68,-67,-69,-70,122,]),',':([27,29,53,54,55,56,63,64,75,76,77,95,99,100,101,102,108,109,111,112,138,155,157,161,162,163,],[42,-41,68,-39,-40,68,79,-32,42,-48,105,-38,-45,-43,-44,135,-50,-31,-34,-33,-47,-37,-42,135,-51,-49,]),'/':([85,87,91,92,125,126,127,129,148,149,150,151,153,154,],[-71,123,-72,-74,123,-72,123,-72,123,-68,123,-69,-70,123,]),'TABLE':([9,10,],[32,33,]),';':([22,26,35,36,45,47,48,52,53,54,56,63,64,83,84,85,87,90,91,92,93,95,97,98,104,109,110,111,112,127,129,130,134,142,143,144,145,146,147,148,149,150,151,152,153,155,164,],[38,40,49,50,59,61,62,66,70,-39,72,80,-32,-58,115,-71,-63,-65,-64,-74,-57,-38,132,133,137,-31,141,-34,-33,-73,-72,-56,156,-53,-54,-62,-61,-60,-59,-66,-68,-67,-69,-55,-70,-37,165,]),'=':([65,85,86,87,90,91,92,125,126,127,129,148,149,150,151,153,],[82,-71,117,-63,-65,-64,-74,-63,-64,-73,-72,-66,-68,-67,-69,-70,]),'<':([85,86,87,90,91,92,125,126,127,129,148,149,150,151,153,],[-71,118,-63,-65,-64,-74,-63,-64,-73,-72,-66,-68,-67,-69,-70,]),'$end':([1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[0,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'STRING':([67,71,73,74,81,82,88,94,113,114,116,117,118,119,135,158,],[90,90,90,99,90,111,90,90,90,90,90,90,90,90,99,99,]),'SHOW':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[17,17,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'INTO':([8,],[30,]),'UPDATE':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[18,18,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'DATABASES':([17,],[36,]),'JOIN':([53,54,56,95,155,],[69,-39,69,-38,-37,]),'WHERE':([52,53,54,56,63,64,95,109,111,112,155,],[67,71,-39,73,81,-32,-38,-31,-34,-33,-37,]),'ID':([2,6,18,30,31,32,33,34,39,41,42,43,51,58,60,67,68,69,71,73,79,81,88,89,94,105,113,114,116,117,118,119,120,121,122,123,128,131,],[26,29,37,44,45,46,47,48,52,54,55,54,65,29,78,92,95,96,92,92,65,92,92,92,92,78,92,92,92,92,92,92,92,92,92,92,92,155,]),'AND':([83,84,85,87,90,91,92,93,97,98,110,124,127,129,130,142,143,144,145,146,147,148,149,150,151,152,153,],[-58,113,-71,-63,-65,-64,-74,-57,113,113,113,113,-73,-72,-56,-53,113,-62,-61,-60,-59,-66,-68,-67,-69,-55,-70,]),'TABLES':([17,],[35,]),'FROM':([24,27,28,29,55,],[39,41,43,-41,-40,]),'DATABASE':([9,10,],[31,34,]),'INT':([78,],[108,]),'BOOLEAN':([67,71,73,81,88,94,113,114,],[93,93,93,93,93,93,93,93,]),'EXIT':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[22,22,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),'VALUES':([44,103,],[57,136,]),'+':([85,87,91,92,125,126,127,129,148,149,150,151,153,154,],[-71,120,-72,-74,120,-72,-73,-72,-66,-68,-67,-69,-70,120,]),'NOT':([67,71,73,81,88,94,113,114,],[94,94,94,94,94,94,94,94,]),'>':([85,86,87,90,91,92,125,126,127,129,148,149,150,151,153,],[-71,119,-63,-65,-64,-74,-63,-64,-73,-72,-66,-68,-67,-69,-70,]),'OR':([83,84,85,87,90,91,92,93,97,98,110,124,127,129,130,142,143,144,145,146,147,148,149,150,151,152,153,],[-58,114,-71,-63,-65,-64,-74,-57,114,114,114,114,-73,-72,-56,-53,-54,-62,-61,-60,-59,-66,-68,-67,-69,-55,-70,]),'DELETE':([0,1,3,4,5,7,11,12,13,14,15,16,19,20,21,22,23,25,38,40,49,50,59,61,62,66,70,72,80,115,132,133,137,141,156,165,],[24,24,-9,-4,-3,-11,-7,-6,-12,-13,-52,-8,-2,-14,-10,-19,-5,-1,-20,-17,-21,-15,-16,-46,-18,-35,-26,-25,-29,-36,-28,-27,-22,-30,-24,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression_set':([0,],[1,]),'expression_comp':([67,71,73,81,88,94,113,114,],[83,83,83,83,83,83,83,83,]),'expression_show_database':([0,1,],[4,4,]),'expression_logic':([67,71,73,81,88,94,113,114,],[84,97,98,110,124,130,142,143,]),'given_value':([74,135,158,],[100,157,100,]),'expression_create_database':([0,1,],[5,5,]),'given_values':([74,158,],[102,161,]),'expression_insert_table':([0,1,],[7,7,]),'tables':([41,43,],[53,56,]),'expression_comp_member':([67,71,73,81,88,94,113,114,116,117,118,119,],[86,86,86,86,86,86,86,86,144,145,146,147,]),'expression_arith':([67,71,73,81,88,89,94,113,114,116,117,118,119,120,121,122,123,128,],[87,87,87,87,125,127,87,87,87,87,87,87,87,148,149,150,151,154,]),'expression_create_table':([0,1,],[3,3,]),'expression_comments':([0,1,],[11,11,]),'expression_exit':([0,1,],[12,12,]),'expression_select_table':([0,1,],[13,13,]),'table_fields_definition':([60,],[77,]),'expression_update_table':([0,1,],[14,14,]),'table_field_definition':([60,105,],[76,138,]),'expression_show_tables':([0,1,],[16,16,]),'column_value':([51,79,],[64,109,]),'column_values':([51,],[63,]),'expression_sql':([0,1,],[19,25,]),'variable':([67,71,73,81,88,89,94,113,114,116,117,118,119,120,121,122,123,128,],[91,91,91,91,126,129,91,91,91,91,91,91,91,129,129,129,129,129,]),'expression_delete_from_table':([0,1,],[20,20,]),'fields':([6,58,],[27,75,]),'expression_drop_table':([0,1,],[21,21,]),'expression_use_database':([0,1,],[23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression_set","S'",1,None,None,None),
  ('expression_set -> expression_set expression_sql','expression_set',2,'p_expression_set','SQLYacc.py',26),
  ('expression_set -> expression_sql','expression_set',1,'p_expression_set','SQLYacc.py',27),
  ('expression_sql -> expression_create_database','expression_sql',1,'p_expression','SQLYacc.py',32),
  ('expression_sql -> expression_show_database','expression_sql',1,'p_expression','SQLYacc.py',33),
  ('expression_sql -> expression_use_database','expression_sql',1,'p_expression','SQLYacc.py',34),
  ('expression_sql -> expression_exit','expression_sql',1,'p_expression','SQLYacc.py',35),
  ('expression_sql -> expression_comments','expression_sql',1,'p_expression','SQLYacc.py',36),
  ('expression_sql -> expression_show_tables','expression_sql',1,'p_expression','SQLYacc.py',37),
  ('expression_sql -> expression_create_table','expression_sql',1,'p_expression','SQLYacc.py',38),
  ('expression_sql -> expression_drop_table','expression_sql',1,'p_expression','SQLYacc.py',39),
  ('expression_sql -> expression_insert_table','expression_sql',1,'p_expression','SQLYacc.py',40),
  ('expression_sql -> expression_select_table','expression_sql',1,'p_expression','SQLYacc.py',41),
  ('expression_sql -> expression_update_table','expression_sql',1,'p_expression','SQLYacc.py',42),
  ('expression_sql -> expression_delete_from_table','expression_sql',1,'p_expression','SQLYacc.py',43),
  ('expression_show_database -> SHOW DATABASES ;','expression_show_database',3,'p_show_dbs','SQLYacc.py',48),
  ('expression_create_database -> CREATE DATABASE ID ;','expression_create_database',4,'p_create_db','SQLYacc.py',54),
  ('expression_use_database -> USE ID ;','expression_use_database',3,'p_use_db','SQLYacc.py',59),
  ('expression_create_database -> DROP DATABASE ID ;','expression_create_database',4,'p_drop_db','SQLYacc.py',64),
  ('expression_exit -> EXIT','expression_exit',1,'p_exit_system','SQLYacc.py',69),
  ('expression_exit -> EXIT ;','expression_exit',2,'p_exit_system','SQLYacc.py',70),
  ('expression_show_tables -> SHOW TABLES ;','expression_show_tables',3,'p_show_tables','SQLYacc.py',77),
  ('expression_create_table -> CREATE TABLE ID ( table_fields_definition ) ;','expression_create_table',7,'p_create_table','SQLYacc.py',83),
  ('expression_insert_table -> INSERT INTO ID ( fields ) VALUES ( given_values ) ;','expression_insert_table',11,'p_insert_table','SQLYacc.py',90),
  ('expression_insert_table -> INSERT INTO ID VALUES ( given_values ) ;','expression_insert_table',8,'p_insert_table','SQLYacc.py',91),
  ('expression_select_table -> SELECT * FROM tables ;','expression_select_table',5,'p_select_table','SQLYacc.py',104),
  ('expression_select_table -> SELECT fields FROM tables ;','expression_select_table',5,'p_select_table','SQLYacc.py',105),
  ('expression_select_table -> SELECT * FROM tables WHERE expression_logic ;','expression_select_table',7,'p_select_table','SQLYacc.py',106),
  ('expression_select_table -> SELECT fields FROM tables WHERE expression_logic ;','expression_select_table',7,'p_select_table','SQLYacc.py',107),
  ('expression_update_table -> UPDATE ID SET column_values ;','expression_update_table',5,'p_update_table','SQLYacc.py',122),
  ('expression_update_table -> UPDATE ID SET column_values WHERE expression_logic ;','expression_update_table',7,'p_update_table','SQLYacc.py',123),
  ('column_values -> column_values , column_value','column_values',3,'p_column_values','SQLYacc.py',137),
  ('column_values -> column_value','column_values',1,'p_column_values','SQLYacc.py',138),
  ('column_value -> ID = NUMBER','column_value',3,'p_column_value','SQLYacc.py',150),
  ('column_value -> ID = STRING','column_value',3,'p_column_value','SQLYacc.py',151),
  ('expression_delete_from_table -> DELETE FROM ID ;','expression_delete_from_table',4,'p_delete_from_table','SQLYacc.py',156),
  ('expression_delete_from_table -> DELETE FROM ID WHERE expression_logic ;','expression_delete_from_table',6,'p_delete_from_table','SQLYacc.py',157),
  ('tables -> tables JOIN ID ON ID','tables',5,'p_tables','SQLYacc.py',170),
  ('tables -> tables , ID','tables',3,'p_tables','SQLYacc.py',171),
  ('tables -> ID','tables',1,'p_tables','SQLYacc.py',172),
  ('fields -> fields , ID','fields',3,'p_fields','SQLYacc.py',189),
  ('fields -> ID','fields',1,'p_fields','SQLYacc.py',190),
  ('given_values -> given_values , given_value','given_values',3,'p_given_values_table','SQLYacc.py',202),
  ('given_values -> given_value','given_values',1,'p_given_values_table','SQLYacc.py',203),
  ('given_value -> NUMBER','given_value',1,'p_given_value_table','SQLYacc.py',215),
  ('given_value -> STRING','given_value',1,'p_given_value_table','SQLYacc.py',216),
  ('expression_drop_table -> DROP TABLE ID ;','expression_drop_table',4,'p_drop_table','SQLYacc.py',221),
  ('table_fields_definition -> table_fields_definition , table_field_definition','table_fields_definition',3,'p_fields_definition','SQLYacc.py',226),
  ('table_fields_definition -> table_field_definition','table_fields_definition',1,'p_fields_definition','SQLYacc.py',227),
  ('table_field_definition -> ID CHAR ( NUMBER )','table_field_definition',5,'p_field_definition','SQLYacc.py',242),
  ('table_field_definition -> ID INT','table_field_definition',2,'p_field_definition','SQLYacc.py',243),
  ('table_field_definition -> ID VARCHAR ( NUMBER )','table_field_definition',5,'p_field_definition','SQLYacc.py',244),
  ('expression_comments -> COMMENT','expression_comments',1,'p_comments','SQLYacc.py',253),
  ('expression_logic -> expression_logic AND expression_logic','expression_logic',3,'p_expression_logic','SQLYacc.py',257),
  ('expression_logic -> expression_logic OR expression_logic','expression_logic',3,'p_expression_logic','SQLYacc.py',258),
  ('expression_logic -> ( expression_logic )','expression_logic',3,'p_expression_logic_group','SQLYacc.py',267),
  ('expression_logic -> NOT expression_logic','expression_logic',2,'p_expression_logic_not','SQLYacc.py',271),
  ('expression_logic -> BOOLEAN','expression_logic',1,'p_expression_logic_member','SQLYacc.py',275),
  ('expression_logic -> expression_comp','expression_logic',1,'p_expression_logic_member','SQLYacc.py',276),
  ('expression_comp -> expression_comp_member > expression_comp_member','expression_comp',3,'p_expression_compare','SQLYacc.py',282),
  ('expression_comp -> expression_comp_member < expression_comp_member','expression_comp',3,'p_expression_compare','SQLYacc.py',283),
  ('expression_comp -> expression_comp_member = expression_comp_member','expression_comp',3,'p_expression_compare','SQLYacc.py',284),
  ('expression_comp -> expression_comp_member NOTEQUALS expression_comp_member','expression_comp',3,'p_expression_compare','SQLYacc.py',285),
  ('expression_comp_member -> expression_arith','expression_comp_member',1,'p_expression_compare_member','SQLYacc.py',298),
  ('expression_comp_member -> variable','expression_comp_member',1,'p_expression_compare_member','SQLYacc.py',299),
  ('expression_comp_member -> STRING','expression_comp_member',1,'p_expression_compare_member','SQLYacc.py',300),
  ('expression_arith -> expression_arith + expression_arith','expression_arith',3,'p_expression_arith','SQLYacc.py',306),
  ('expression_arith -> expression_arith - expression_arith','expression_arith',3,'p_expression_arith','SQLYacc.py',307),
  ('expression_arith -> expression_arith * expression_arith','expression_arith',3,'p_expression_arith','SQLYacc.py',308),
  ('expression_arith -> expression_arith / expression_arith','expression_arith',3,'p_expression_arith','SQLYacc.py',309),
  ('expression_arith -> ( expression_arith )','expression_arith',3,'p_expression_arith_group','SQLYacc.py',323),
  ('expression_arith -> NUMBER','expression_arith',1,'p_expression_arith_member','SQLYacc.py',327),
  ('expression_arith -> variable','expression_arith',1,'p_expression_arith_member','SQLYacc.py',328),
  ('expression_arith -> - expression_arith','expression_arith',2,'p_expression_arith_minus','SQLYacc.py',333),
  ('variable -> ID','variable',1,'p_variable','SQLYacc.py',337),
]