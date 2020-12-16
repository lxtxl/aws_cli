#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-instance-access-control-attribute-configuration.html
if __name__ == '__main__':
    """
	create-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-instance-access-control-attribute-configuration.html
	delete-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-instance-access-control-attribute-configuration.html
	describe-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-instance-access-control-attribute-configuration.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed.
    # instance-access-control-attribute-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sso-admin", "update-instance-access-control-attribute-configuration", "instance-arn", "instance-access-control-attribute-configuration", add_option_dict)
