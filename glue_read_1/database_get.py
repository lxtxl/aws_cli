#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-database.html
if __name__ == '__main__':
    """
	create-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-database.html
	get-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html
	update-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-database.html
    """

    parameter_display_string = """
    # name : The name of the database to retrieve. For Hive compatibility, this should be all lowercase.
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

    execute_one_parameter("glue", "get-database", "name", add_option_dict)