#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-column-statistics-for-table.html
if __name__ == '__main__':
    """
	delete-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-column-statistics-for-table.html
	update-column-statistics-for-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-column-statistics-for-table.html
    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the partitions reside.
    # table-name : The name of the partitionsâ table.
    """

    execute_two_parameter("glue", "get-column-statistics-for-table", "database-name", "table-name", parameter_display_string)