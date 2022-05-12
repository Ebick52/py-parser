# py-parser
Parser function to investigate wether a specific sentence is produced by a grammer or not! The approach to find answer is through BFS on the grammar's derivation tree.

Notes:

- insert every transition of grammar as left_side:right_side1|rightside2|...
- first transition always starts with S
- target sentence has to be an empty string or contain only lowercase alphabet
- for an empty production you can use "lambda" as a right_side of grammar or just leave it empty
