#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html
if __name__ == '__main__':
    """
	deprecate-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-activity-type.html
	describe-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html
	list-activity-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-activity-types.html
	undeprecate-activity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-activity-type.html
    """

    parameter_display_string = """
    # domain : The name of the domain in which this activity is to be registered.
    # name : The name of the activity type within the domain.
The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    # activity-version : The version of the activity type.

Note
The activity type consists of the name and version, the combination of which must be unique within the domain.

The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("swf", "register-activity-type", "domain", "name", "activity-version", add_option_dict)
