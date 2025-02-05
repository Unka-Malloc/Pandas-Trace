from pysdql.query.tpch.const import (ORDERS_TYPE, LINEITEM_TYPE)

from pysdql.extlib.sdqlpy.sdql_lib import *


@sdql_compile({"ord": ORDERS_TYPE, "li": LINEITEM_TYPE})
def query(ord, li):

    # Insert
    orders_0 = ord.sum(lambda x: ({x[0]: x[1]}) if (((x[0].o_orderdate >= 19930701) * (x[0].o_orderdate < 19931001))) else (None))
    
    lineitem_orders_isin_pre_ops = li.sum(lambda x: ({x[0]: x[1]}) if (x[0].l_commitdate < x[0].l_receiptdate) else (None))
    
    lineitem_orders_isin_build_index = lineitem_orders_isin_pre_ops.sum(lambda x: {x[0].l_orderkey: True})
    
    orders_1 = orders_0.sum(lambda x: ({x[0]: x[1]}) if (lineitem_orders_isin_build_index[x[0].o_orderkey] != None) else (None))
    
    orders_2 = orders_1.sum(lambda x: {record({"o_orderpriority": x[0].o_orderpriority}): record({"order_count": (1.0) if (x[0].o_orderpriority != None) else (0.0)})})
    
    orders_3 = orders_2.sum(lambda x: {x[0].concat(x[1]): True})
    
    orders_4 = orders_3.sum(lambda x: {x[0]: {record({"order_count": x[0].order_count}): True}})
    
    results = orders_4.sum(lambda x: x[1])
    
    # Complete

    return results
