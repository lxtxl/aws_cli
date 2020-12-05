#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things.html
if __name__ == '__main__':
    """
	create-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing.html
	delete-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing.html
	describe-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing.html
	register-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-thing.html
	update-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iot", "list-things", add_option_dict)