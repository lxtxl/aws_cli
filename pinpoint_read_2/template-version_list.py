#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/list-template-versions.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # template-name : The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    # template-type : The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
    """

    execute_two_parameter("pinpoint", "list-template-versions", "template-name", "template-type", parameter_display_string)