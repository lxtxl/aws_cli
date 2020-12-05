#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/describe-contact.html
if __name__ == '__main__':
    """
	cancel-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/cancel-contact.html
	list-contacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-contacts.html
	reserve-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/reserve-contact.html
    """

    parameter_display_string = """
    # contact-id : UUID of a contact.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("groundstation", "describe-contact", "contact-id", add_option_dict)