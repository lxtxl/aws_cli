#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-tables.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table.html
	get-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html
	search-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/search-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html
    """

    parameter_display_string = """
    # database-name : The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("glue", "get-tables", "database-name", add_option_dict)