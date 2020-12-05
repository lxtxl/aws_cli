#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html
if __name__ == '__main__':
    """
	create-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html
	delete-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-endpoint-group.html
	describe-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html
	list-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html
    """

    parameter_display_string = """
    # endpoint-group-arn : The Amazon Resource Name (ARN) of the endpoint group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("globalaccelerator", "update-endpoint-group", "endpoint-group-arn", add_option_dict)





