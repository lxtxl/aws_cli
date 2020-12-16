#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-code-signing-config.html
if __name__ == '__main__':
    """
	create-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-code-signing-config.html
	delete-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-code-signing-config.html
	list-code-signing-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-code-signing-configs.html
	update-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-code-signing-config.html
    """

    parameter_display_string = """
    # code-signing-config-arn : The The Amazon Resource Name (ARN) of the code signing configuration.
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

    execute_one_parameter("lambda", "get-code-signing-config", "code-signing-config-arn", add_option_dict)