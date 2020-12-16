#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-contact-lists.html
if __name__ == '__main__':
    """
	create-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-contact-list.html
	delete-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-contact-list.html
	get-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-contact-list.html
	update-contact-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-contact-list.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("sesv2", "list-contact-lists", add_option_dict)