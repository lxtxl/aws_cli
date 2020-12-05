#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-activity.html
if __name__ == '__main__':
    """
	delete-activity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-activity.html
	describe-activity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-activity.html
	list-activities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-activities.html
    """

    parameter_display_string = """
    # name : The name of the activity to create. This name must be unique for your AWS account and region for 90 days. For more information, see Limits Related to State Machine Executions in the AWS Step Functions Developer Guide .
A name must not contain:

white space
brackets < > { } [ ]
wildcard characters ? *
special characters " # % \ ^ | ~ ` $ & , ; : /
control characters (U+0000-001F , U+007F-009F )

To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("stepfunctions", "create-activity", "name", add_option_dict)





