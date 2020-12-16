#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-license.html
if __name__ == '__main__':
    """
	checkout-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/checkout-license.html
	create-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license.html
	get-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license.html
	list-licenses : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-licenses.html
    """

    parameter_display_string = """
    # license-arn : Amazon Resource Name (ARN) of the license.
    # source-version : Current version of the license.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("license-manager", "delete-license", "license-arn", "source-version", add_option_dict)
