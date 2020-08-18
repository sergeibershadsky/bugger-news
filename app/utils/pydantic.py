from pydantic.networks import AnyUrl


class SqliteDsn(AnyUrl):
    allowed_schemes = {'sqlite'}
