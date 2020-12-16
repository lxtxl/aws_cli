#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/stop-contact-recording.html
if __name__ == '__main__':
    """
	resume-contact-recording : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/resume-contact-recording.html
	start-contact-recording : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-contact-recording.html
	suspend-contact-recording : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/suspend-contact-recording.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # contact-id : The identifier of the contact.
    # initial-contact-id : The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "stop-contact-recording", "instance-id", "contact-id", "initial-contact-id", add_option_dict)
