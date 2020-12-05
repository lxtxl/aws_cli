#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html
if __name__ == '__main__':
    """
	delete-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html
	detach-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html
	get-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user-policy.html
	list-user-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html
	put-user-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html
    """

    parameter_display_string = """
    # user-name : The name (friendly name, not ARN) of the IAM user to attach the policy to.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-arn : The Amazon Resource Name (ARN) of the IAM policy you want to attach.
For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "attach-user-policy", "user-name", "policy-arn", add_option_dict)
