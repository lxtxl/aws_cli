#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html
if __name__ == '__main__':
    """
	cancel-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/cancel-change-set.html
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html
	start-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html
    """

    parameter_display_string = """
    # catalog : The catalog related to the request. Fixed value: AWSMarketplace
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

    execute_one_parameter("marketplace-catalog", "list-change-sets", "catalog", add_option_dict)