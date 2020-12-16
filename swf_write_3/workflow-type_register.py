#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html
if __name__ == '__main__':
    """
	deprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-workflow-type.html
	describe-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html
	list-workflow-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html
	undeprecate-workflow-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html
    """

    parameter_display_string = """
    # domain : The name of the domain in which to register the workflow type.
    # name : The name of the workflow type.
The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    # workflow-version : The version of the workflow type.

Note
The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the  ListWorkflowTypes action.

The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("swf", "register-workflow-type", "domain", "name", "workflow-version", add_option_dict)
