#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/cancel-change-set.html
if __name__ == '__main__':
    """
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html
	start-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html
    """

    parameter_display_string = """
    # catalog : Required. The catalog related to the request. Fixed value: AWSMarketplace .
    # change-set-id : Required. The unique identifier of the StartChangeSet request that you want to cancel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("marketplace-catalog", "cancel-change-set", "catalog", "change-set-id", add_option_dict)
