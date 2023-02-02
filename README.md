# PySDQL
 
`data_matcher` SDQL -> Python

`data_parser` File -> Python

`data_interpreter` Python -> SDQL

`DataFrame` mutable = False

If DataFrame is created from data, including `DataFrame(data=)` and `read_csv()`

then `mutable = False`

else `mutable = True`

Reason: Other DataFrames are intermediate pipes between input and output. 

`DictEl` and `RecEl`

If `mutable == True`: intermediate step

else if `mutable == False`: data collection

Only `data_matcher.from_expr()` will set `mutable == False`
1. `from_record()`
2. `from_dict()`

Split `expr` and `sdql_expr`

`expr => __str__()`: `str(x) | print(x)`

`sdql_expr => __repr__()`: `repr(x) | eval(x)`
