#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-partition-index.html
if __name__ == '__main__':
    """
	create-partition-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-partition-index.html
	get-partition-indexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partition-indexes.html
    """

    parameter_display_string = """
    # database-name : Specifies the name of a database from which you want to delete a partition index.
    # table-name : Specifies the name of a table from which you want to delete a partition index.
    # index-name : The name of the partition index to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "delete-partition-index", "database-name", "table-name", "index-name", add_option_dict)
