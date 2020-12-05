#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-event-invoke-config.html
if __name__ == '__main__':
    """
	delete-function-event-invoke-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-event-invoke-config.html
	list-function-event-invoke-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-event-invoke-configs.html
	put-function-event-invoke-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html
	update-function-event-invoke-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html
    """

    parameter_display_string = """
    # function-name : The name of the Lambda function, version, or alias.

Name formats


Function name - my-function (name-only), my-function:v1 (with alias).
Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function .
Partial ARN - 123456789012:function:my-function .

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
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

    execute_one_parameter("lambda", "get-function-event-invoke-config", "function-name", add_option_dict)