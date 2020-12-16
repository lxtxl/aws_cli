#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html
if __name__ == '__main__':
    """
	delete-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine.html
	describe-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html
	list-state-machines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machines.html
	update-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine.html
    """

    parameter_display_string = """
    # name : The name of the state machine.
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.
    # definition : The Amazon States Language definition of the state machine. See Amazon States Language .
    # role-arn : The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("stepfunctions", "create-state-machine", "name", "definition", "role-arn", add_option_dict)
