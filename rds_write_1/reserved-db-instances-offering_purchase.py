#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/purchase-reserved-db-instances-offering.html
if __name__ == '__main__':
    """
	describe-reserved-db-instances-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-reserved-db-instances-offerings.html
    """

    parameter_display_string = """
    # reserved-db-instances-offering-id : The ID of the Reserved DB instance offering to purchase.
Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "purchase-reserved-db-instances-offering", "reserved-db-instances-offering-id", add_option_dict)





