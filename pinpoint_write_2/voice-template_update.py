#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-voice-template.html
if __name__ == '__main__':
    """
	create-voice-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-voice-template.html
	delete-voice-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-voice-template.html
	get-voice-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-voice-template.html
    """

    parameter_display_string = """
    # template-name : The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    # voice-template-request : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint", "update-voice-template", "template-name", "voice-template-request", add_option_dict)
