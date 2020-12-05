#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html
if __name__ == '__main__':
    """
	delete-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role.html
	get-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html
	list-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-roles.html
	tag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html
	untag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html
	update-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html
    """

    parameter_display_string = """
    # role-name : The name of the role to create.
IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both âMyResourceâ and âmyresourceâ.
    # assume-role-policy-document : The trust relationship policy document that grants an entity permission to assume the role.
In IAM, you must provide a JSON policy that has been converted to a string. However, for AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.
The regex pattern used to validate this parameter is a string of characters consisting of the following:

Any printable ASCII character ranging from the space character (\u0020 ) through the end of the ASCII character range
The printable characters in the Basic Latin and Latin-1 Supplement character set (through \u00FF )
The special characters tab (\u0009 ), line feed (\u000A ), and carriage return (\u000D )

Upon success, the response includes the same trust policy in JSON format.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "create-role", "role-name", "assume-role-policy-document", add_option_dict)
