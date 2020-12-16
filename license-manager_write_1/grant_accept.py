#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/accept-grant.html
if __name__ == '__main__':
    """
	create-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-grant.html
	delete-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-grant.html
	get-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-grant.html
	reject-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/reject-grant.html
    """

    parameter_display_string = """
    # grant-arn : Amazon Resource Name (ARN) of the grant.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("license-manager", "accept-grant", "grant-arn", add_option_dict)





