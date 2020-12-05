#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html
if __name__ == '__main__':
    """
	create-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html
	get-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html
	list-data-catalogs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html
	update-data-catalog : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-data-catalog.html
    """

    parameter_display_string = """
    # name : The name of the data catalog to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("athena", "delete-data-catalog", "name", add_option_dict)





