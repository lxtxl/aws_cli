#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html
if __name__ == '__main__':
    """
	attach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html
	delete-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html
	detach-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html
	get-group-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group-policy.html
	list-group-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html
    """

    parameter_display_string = """
    # group-name : The name of the group to associate the policy with.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-.
    # policy-name : The name of the policy document.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # policy-document : The policy document.
You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iam", "put-group-policy", "group-name", "policy-name", "policy-document", add_option_dict)
