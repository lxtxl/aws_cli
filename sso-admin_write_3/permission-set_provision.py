#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/provision-permission-set.html
if __name__ == '__main__':
    """
	create-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-permission-set.html
	delete-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/delete-permission-set.html
	describe-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set.html
	list-permission-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-sets.html
	update-permission-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/update-permission-set.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # permission-set-arn : The ARN of the permission set.
    # target-type : The entity type for which the assignment will be created.
Possible values:

AWS_ACCOUNT
ALL_PROVISIONED_ACCOUNTS
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sso-admin", "provision-permission-set", "instance-arn", "permission-set-arn", "target-type", add_option_dict)
