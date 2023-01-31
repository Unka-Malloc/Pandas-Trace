import pandas as pd

from pysdql.query.tpch.const import (
    DATAPATH,
    LINEITEM_COLS,
    ORDERS_COLS,
    CUSTOMER_COLS,
    NATION_COLS,
    REGION_COLS,
    PART_COLS,
    SUPPLIER_COLS,
    PARTSUPP_COLS
)

from pysdql.query.tpch.template import *

# show all columns
pd.set_option('display.max_columns', None)
# suppress SettingWithCopyWarning
pd.set_option('mode.chained_assignment', None)


def q1():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)

    result = tpch_q1(lineitem)

    return result


def q3():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)

    result = tpch_q3(lineitem, customer, orders)

    return result


def q4():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)

    result = tpch_q4(orders, lineitem)

    return result

def q5():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    nation = pd.read_csv(rf'{DATAPATH}/nation.tbl', sep='|', index_col=False, header=None, names=NATION_COLS)
    region = pd.read_csv(rf'{DATAPATH}/region.tbl', sep='|', index_col=False, header=None, names=REGION_COLS)
    supplier = pd.read_csv(rf'{DATAPATH}/supplier.tbl', sep='|', index_col=False, header=None, names=SUPPLIER_COLS)

    result = tpch_q5(lineitem, customer, orders, region, nation, supplier)

    return result

def q6():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)

    result = tpch_q6(lineitem)

    return result

def q7():
    supplier = pd.read_csv(rf'{DATAPATH}/supplier.tbl', sep='|', index_col=False, header=None, names=SUPPLIER_COLS)
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS, parse_dates=["l_shipdate"])
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    nation = pd.read_csv(rf'{DATAPATH}/nation.tbl', sep='|', index_col=False, header=None, names=NATION_COLS)

    result = tpch_q7(supplier, lineitem, orders, customer, nation)

    return result

def q8():
    part = pd.read_csv(rf'{DATAPATH}/part.tbl', sep='|', index_col=False, header=None, names=PART_COLS)
    supplier = pd.read_csv(rf'{DATAPATH}/supplier.tbl', sep='|', index_col=False, header=None, names=SUPPLIER_COLS)
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS, parse_dates=['o_orderdate'])
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    nation = pd.read_csv(rf'{DATAPATH}/nation.tbl', sep='|', index_col=False, header=None, names=NATION_COLS)
    region = pd.read_csv(rf'{DATAPATH}/region.tbl', sep='|', index_col=False, header=None, names=REGION_COLS)

    result = tpch_q8(part, supplier, lineitem, orders, customer, nation, region)

    return result

def q10():
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    nation = pd.read_csv(rf'{DATAPATH}/nation.tbl', sep='|', index_col=False, header=None, names=NATION_COLS)

    result = tpch_q10(customer, orders, lineitem, nation)

    return result

def q12():
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)

    result = tpch_q12(orders, lineitem)

    return result

def q13():
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)

    result = tpch_q13(customer, orders)

    return result

def q14():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    part = pd.read_csv(rf'{DATAPATH}/part.tbl', sep='|', index_col=False, header=None, names=PART_COLS)

    result = tpch_q14(lineitem, part)

    return result


def q15():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    supplier = pd.read_csv(rf'{DATAPATH}/supplier.tbl', sep='|', index_col=False, header=None, names=SUPPLIER_COLS)

    result = tpch_q15(lineitem, supplier)

    return result


def q16():
    partsupp = pd.read_csv(rf'{DATAPATH}/partsupp.tbl', sep='|', index_col=False, header=None, names=PARTSUPP_COLS)
    part = pd.read_csv(rf'{DATAPATH}/part.tbl', sep='|', index_col=False, header=None, names=PART_COLS)
    supplier = pd.read_csv(rf'{DATAPATH}/supplier.tbl', sep='|', index_col=False, header=None, names=SUPPLIER_COLS)

    result = tpch_q16(partsupp, part, supplier)

    return result

def q17():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    part = pd.read_csv(rf'{DATAPATH}/part.tbl', sep='|', index_col=False, header=None, names=PART_COLS)

    result = tpch_q17(lineitem, part)

    return result


def q18():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    customer = pd.read_csv(rf'{DATAPATH}/customer.tbl', sep='|', index_col=False, header=None, names=CUSTOMER_COLS)
    orders = pd.read_csv(rf'{DATAPATH}/orders.tbl', sep='|', index_col=False, header=None, names=ORDERS_COLS)

    result = tpch_q18(lineitem, customer, orders)

    return result


def q19():
    lineitem = pd.read_csv(rf'{DATAPATH}/lineitem.tbl', sep='|', index_col=False, header=None, names=LINEITEM_COLS)
    part = pd.read_csv(rf'{DATAPATH}/part.tbl', sep='|', index_col=False, header=None, names=PART_COLS)

    result = tpch_q19(lineitem, part)

    return result
