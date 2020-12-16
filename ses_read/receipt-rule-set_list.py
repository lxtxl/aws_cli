#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-receipt-rule-sets.html
if __name__ == '__main__':
    """
	clone-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/clone-receipt-rule-set.html
	create-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-receipt-rule-set.html
	delete-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-receipt-rule-set.html
	describe-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-receipt-rule-set.html
	reorder-receipt-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/reorder-receipt-rule-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ses", "list-receipt-rule-sets", add_option_dict)