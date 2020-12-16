#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-instance-access-control-attribute-configuration.html
if __name__ == '__main__':
    """
	create-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-instance-access-control-attribute-configuration.html
	delete-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-instance-access-control-attribute-configuration.html
	update-instance-access-control-attribute-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-instance-access-control-attribute-configuration.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed.
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

    execute_one_parameter("sso-admin", "describe-instance-access-control-attribute-configuration", "instance-arn", add_option_dict)