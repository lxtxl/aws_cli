#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition-indexes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : Specifies the name of a database from which you want to retrieve partition indexes.
    # table-name : Specifies the name of a table for which you want to retrieve the partition indexes.
    """

    execute_two_parameter("glue", "get-partition-indexes", "database-name", "table-name", parameter_display_string)