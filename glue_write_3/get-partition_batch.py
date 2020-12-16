#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-get-partition.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The name of the catalog database where the partitions reside.
    # table-name : The name of the partitionsâ table.
    # partitions-to-get : A list of partition values identifying the partitions to retrieve.
(structure)

Contains a list of values defining partitions.
Values -> (list)

The list of values.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "batch-get-partition", "database-name", "table-name", "partitions-to-get", add_option_dict)
