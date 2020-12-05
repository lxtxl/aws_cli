#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/update-subnet-group.html
if __name__ == '__main__':
    """
	create-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-subnet-group.html
	delete-subnet-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-subnet-group.html
	describe-subnet-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-subnet-groups.html
    """

    parameter_display_string = """
    # subnet-group-name : The name of the subnet group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dax", "update-subnet-group", "subnet-group-name", add_option_dict)





