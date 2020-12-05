#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-distribution-configuration.html
if __name__ == '__main__':
    """
	create-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html
	get-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html
	list-distribution-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html
	update-distribution-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html
    """

    parameter_display_string = """
    # distribution-configuration-arn : The Amazon Resource Name (ARN) of the distribution configuration to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("imagebuilder", "delete-distribution-configuration", "distribution-configuration-arn", add_option_dict)





