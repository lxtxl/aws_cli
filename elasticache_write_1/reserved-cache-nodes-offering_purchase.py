#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/purchase-reserved-cache-nodes-offering.html
if __name__ == '__main__':
    """
	describe-reserved-cache-nodes-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-reserved-cache-nodes-offerings.html
    """

    parameter_display_string = """
    # reserved-cache-nodes-offering-id : The ID of the reserved cache node offering to purchase.
Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "purchase-reserved-cache-nodes-offering", "reserved-cache-nodes-offering-id", add_option_dict)





