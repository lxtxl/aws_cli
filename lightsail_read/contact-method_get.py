#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-contact-methods.html
if __name__ == '__main__':
    """
	create-contact-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-contact-method.html
	delete-contact-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-contact-method.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("lightsail", "get-contact-methods", add_option_dict)