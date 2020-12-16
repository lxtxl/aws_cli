#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-template-active-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # template-active-version-request : 
    # template-name : The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    # template-type : The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("pinpoint", "update-template-active-version", "template-active-version-request", "template-name", "template-type", add_option_dict)
