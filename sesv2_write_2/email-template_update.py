#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-email-template.html
if __name__ == '__main__':
    """
	create-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-email-template.html
	delete-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-email-template.html
	get-email-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-email-template.html
	list-email-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-email-templates.html
    """

    parameter_display_string = """
    # template-name : The name of the template you want to update.
    # template-content : The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sesv2", "update-email-template", "template-name", "template-content", add_option_dict)
