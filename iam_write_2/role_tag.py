#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html
if __name__ == '__main__':
    """
	create-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html
	delete-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role.html
	get-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html
	list-roles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-roles.html
	untag-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html
	update-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html
    """

    parameter_display_string = """
    # role-name : The name of the role that you want to add tags to.
This parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    # tags : The list of tags that you want to attach to the role. Each tag consists of a key name and an associated value. You can specify this with a JSON string.
(structure)

A structure that represents user-provided metadata that can be associated with a resource such as an IAM user or role. For more information about tagging, see Tagging IAM Identities in the IAM User Guide .
Key -> (string)

The key name that can be used to look up or retrieve the associated value. For example, Department or Cost Center are common choices.

Value -> (string)

The value associated with this tag. For example, tags with a key name of Department could have values such as Human Resources , Accounting , and Support . Tags with a key name of Cost Center might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.

Note
AWS always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iam", "tag-role", "role-name", "tags", add_option_dict)
