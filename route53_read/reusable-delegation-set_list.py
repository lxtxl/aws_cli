#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-reusable-delegation-sets.html
if __name__ == '__main__':
    """
	create-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-reusable-delegation-set.html
	delete-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-reusable-delegation-set.html
	get-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-reusable-delegation-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("route53", "list-reusable-delegation-sets", add_option_dict)