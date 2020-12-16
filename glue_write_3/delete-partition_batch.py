#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-delete-partition.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The name of the catalog database in which the table in question resides.
    # table-name : The name of the table that contains the partitions to be deleted.
    # partitions-to-delete : A list of PartitionInput structures that define the partitions to be deleted.
(structure)

Contains a list of values defining partitions.
Values -> (list)

The list of values.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "batch-delete-partition", "database-name", "table-name", "partitions-to-delete", add_option_dict)
