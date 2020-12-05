#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html
if __name__ == '__main__':
    """
	delete-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-endpoint-group.html
	describe-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html
	list-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html
	update-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html
    """

    parameter_display_string = """
    # listener-arn : The Amazon Resource Name (ARN) of the listener.
    # endpoint-group-region : The AWS Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("globalaccelerator", "create-endpoint-group", "listener-arn", "endpoint-group-region", add_option_dict)
