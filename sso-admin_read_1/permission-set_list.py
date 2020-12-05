#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-sets.html
if __name__ == '__main__':
    """
	create-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-permission-set.html
	delete-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-permission-set.html
	describe-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set.html
	provision-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/provision-permission-set.html
	update-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-permission-set.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
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

    execute_one_parameter("sso-admin", "list-permission-sets", "instance-arn", add_option_dict)