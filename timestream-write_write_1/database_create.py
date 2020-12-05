#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-database.html
if __name__ == '__main__':
    """
	delete-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-database.html
	describe-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-database.html
	list-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-databases.html
	update-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-database.html
    """

    parameter_display_string = """
    # database-name : The name of the Timestream database.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("timestream-write", "create-database", "database-name", add_option_dict)





