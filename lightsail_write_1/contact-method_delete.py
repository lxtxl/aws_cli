#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-contact-method.html
if __name__ == '__main__':
    """
	create-contact-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-contact-method.html
	get-contact-methods : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-contact-methods.html
    """

    parameter_display_string = """
    # protocol : The protocol that will be deleted, such as Email or SMS (text messaging).

Note
To delete an Email and an SMS contact method if you added both, you must run separate DeleteContactMethod actions to delete each protocol.

Possible values:

Email
SMS
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-contact-method", "protocol", add_option_dict)





