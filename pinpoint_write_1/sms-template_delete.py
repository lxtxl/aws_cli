#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-sms-template.html
if __name__ == '__main__':
    """
	create-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-sms-template.html
	get-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-sms-template.html
	update-sms-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-sms-template.html
    """

    parameter_display_string = """
    # template-name : The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint", "delete-sms-template", "template-name", add_option_dict)





