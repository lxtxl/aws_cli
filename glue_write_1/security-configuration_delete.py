#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-security-configuration.html
if __name__ == '__main__':
    """
	create-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-security-configuration.html
	get-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-security-configuration.html
	get-security-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-security-configurations.html
    """

    parameter_display_string = """
    # name : The name of the security configuration to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "delete-security-configuration", "name", add_option_dict)





