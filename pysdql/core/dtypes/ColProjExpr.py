from pysdql.core.dtypes.sdql_ir import RecConsExpr


class ColProjExpr:
    def __init__(self, proj_on, proj_cols):
        self.proj_on = proj_on
        self.proj_cols = proj_cols

    @property
    def cols(self):
        return RecConsExpr([(col, self.proj_on.key_access(col)) for col in self.proj_cols])

    @property
    def sdql_ir(self):
        return self.cols

    @property
    def op_name_suffix(self):
        return f'_proj'

    def __repr__(self):
        return str({
            'proj_on': self.proj_on,
            'proj_cols': self.proj_cols
        })

