#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	untag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    parameter_display_string = """
    # user-name : The name of the user that you want to add tags to.
This parameter accepts (through its regex pattern ) a string of characters that consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@-
    # tags : The list of tags that you want to attach to the user. Each tag consists of a key name and an associated value.
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
    write_two_parameter("iam", "tag-user", "user-name", "tags", add_option_dict)
