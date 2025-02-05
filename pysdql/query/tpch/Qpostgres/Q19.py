from pysdql.query.tpch.const import (LINEITEM_TYPE, PART_TYPE)

from pysdql.extlib.sdqlpy.sdql_lib import *

@sdql_compile({"li": LINEITEM_TYPE, "pa": PART_TYPE})
def query(li, pa):

    # Insert
    air = "AIR"
    airreg = "AIR REG"
    deliverinperson = "DELIVER IN PERSON"
    brand12 = "Brand#12"
    smcase = "SM CASE"
    smbox = "SM BOX"
    smpack = "SM PACK"
    smpkg = "SM PKG"
    brand23 = "Brand#23"
    medbag = "MED BAG"
    medbox = "MED BOX"
    medpkg = "MED PKG"
    medpack = "MED PACK"
    brand34 = "Brand#34"
    lgcase = "LG CASE"
    lgbox = "LG BOX"
    lgpack = "LG PACK"
    lgpkg = "LG PKG"
    lineitem_part_build_pre_ops = li.sum(lambda x: ({x[0]: x[1]}) if (((((((x[0].l_shipmode == airreg) + (x[0].l_shipmode == air))) * (x[0].l_shipinstruct == deliverinperson))) * (((((((x[0].l_quantity >= 1) * (x[0].l_quantity <= 11))) + (((x[0].l_quantity >= 10) * (x[0].l_quantity <= 20))))) + (((x[0].l_quantity >= 20) * (x[0].l_quantity <= 30))))))) else (None))
    
    lineitem_part_probe_pre_ops = pa.sum(lambda x: ({x[0]: x[1]}) if (((x[0].p_size >= 1) * (((((((((x[0].p_brand == brand12) * (((((((x[0].p_container == smpkg) + (x[0].p_container == smpack))) + (x[0].p_container == smcase))) + (x[0].p_container == smbox))))) * (x[0].p_size <= 5))) + (((((x[0].p_brand == brand23) * (((((((x[0].p_container == medpack) + (x[0].p_container == medpkg))) + (x[0].p_container == medbag))) + (x[0].p_container == medbox))))) * (x[0].p_size <= 10))))) + (((((x[0].p_brand == brand34) * (((((((x[0].p_container == lgpkg) + (x[0].p_container == lgpack))) + (x[0].p_container == lgcase))) + (x[0].p_container == lgbox))))) * (x[0].p_size <= 15))))))) else (None))
    
    lineitem_part_build_nest_dict = lineitem_part_build_pre_ops.sum(lambda x: {x[0].l_partkey: sr_dict({x[0]: x[1]})})
    
    lineitem_part_0 = lineitem_part_probe_pre_ops.sum(lambda x: (lineitem_part_build_nest_dict[x[0].p_partkey].sum(lambda y: {x[0].concat(y[0]): True})
    ) if (lineitem_part_build_nest_dict[x[0].p_partkey] != None) else (None))
    
    lineitem_part_1 = lineitem_part_0.sum(lambda x: ({x[0]: x[1]}) if (((((((((((((x[0].p_brand == brand12) * (((((((x[0].p_container == smpkg) + (x[0].p_container == smpack))) + (x[0].p_container == smcase))) + (x[0].p_container == smbox))))) * (x[0].l_quantity >= 1))) * (x[0].l_quantity <= 11))) * (x[0].p_size <= 5))) + (((((((((x[0].p_brand == brand23) * (((((((x[0].p_container == medpack) + (x[0].p_container == medpkg))) + (x[0].p_container == medbag))) + (x[0].p_container == medbox))))) * (x[0].l_quantity >= 10))) * (x[0].l_quantity <= 20))) * (x[0].p_size <= 10))))) + (((((((((x[0].p_brand == brand34) * (((((((x[0].p_container == lgpkg) + (x[0].p_container == lgpack))) + (x[0].p_container == lgcase))) + (x[0].p_container == lgbox))))) * (x[0].l_quantity >= 20))) * (x[0].l_quantity <= 30))) * (x[0].p_size <= 15))))) else (None))
    
    lineitem_part_2 = lineitem_part_1.sum(lambda x: ((x[0].l_extendedprice) * (((1) - (x[0].l_discount)))))
    
    results = {record({"revenue": lineitem_part_2}): True}
    # Complete

    return results
