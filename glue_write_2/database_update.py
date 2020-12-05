#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-database.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-database.html
	get-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html
	get-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html
    """

    parameter_display_string = """
    # name : The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.
    # database-input : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "update-database", "name", "database-input", add_option_dict)
