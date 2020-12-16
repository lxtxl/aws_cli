#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-partition-index.html
if __name__ == '__main__':
    """
	delete-partition-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition-index.html
	get-partition-indexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition-indexes.html
    """

    parameter_display_string = """
    # database-name : Specifies the name of a database in which you want to create a partition index.
    # table-name : Specifies the name of a table in which you want to create a partition index.
    # partition-index : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "create-partition-index", "database-name", "table-name", "partition-index", add_option_dict)
