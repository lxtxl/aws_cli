#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html
if __name__ == '__main__':
    """
	create-activation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html
	describe-activations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-activations.html
    """

    parameter_display_string = """
    # activation-id : The ID of the activation that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "delete-activation", "activation-id", add_option_dict)





