#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html
if __name__ == '__main__':
    """
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table.html
	get-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html
	get-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-tables.html
	search-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/search-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html
    """

    parameter_display_string = """
    # database-name : The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.
    # table-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "create-table", "database-name", "table-input", add_option_dict)
