#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-custom-verification-email-template.html
if __name__ == '__main__':
    """
	create-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-custom-verification-email-template.html
	get-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-custom-verification-email-template.html
	list-custom-verification-email-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-custom-verification-email-templates.html
	update-custom-verification-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-custom-verification-email-template.html
    """

    parameter_display_string = """
    # template-name : The name of the custom verification email template that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "delete-custom-verification-email-template", "template-name", add_option_dict)





