
__package_name__ = "ksql"
__ksql_server_version__ = "0.3"
__ksql_api_version__ = "0.2.0"
__version__ = __ksql_server_version__ + "." + __ksql_api_version__

from ksql.client import KSQLAPI
from ksql.builder import SQLBuilder
