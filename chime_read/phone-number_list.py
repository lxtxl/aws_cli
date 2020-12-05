#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-numbers.html
if __name__ == '__main__':
    """
	delete-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-phone-number.html
	get-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number.html
	restore-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/restore-phone-number.html
	update-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("chime", "list-phone-numbers", add_option_dict)