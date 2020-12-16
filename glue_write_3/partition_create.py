#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-partition.html
if __name__ == '__main__':
    """
	delete-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition.html
	get-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition.html
	get-partitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partitions.html
	update-partition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-partition.html
    """

    parameter_display_string = """
    # database-name : The name of the metadata database in which the partition is to be created.
    # table-name : The name of the metadata table in which the partition is to be created.
    # partition-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "create-partition", "database-name", "table-name", "partition-input", add_option_dict)
