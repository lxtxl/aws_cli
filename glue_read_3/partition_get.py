#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition.html
if __name__ == '__main__':
    """
	create-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-partition.html
	delete-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition.html
	get-partitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partitions.html
	update-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-partition.html
    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the partition resides.
    # table-name : The name of the partitionâs table.
    """

    execute_two_parameter("glue", "get-partition", "database-name", "table-name", parameter_display_string)