#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/purchase-reserved-node-offering.html
if __name__ == '__main__':
    """
	describe-reserved-node-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-node-offerings.html
    """

    parameter_display_string = """
    # reserved-node-offering-id : The unique identifier of the reserved node offering you want to purchase.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "purchase-reserved-node-offering", "reserved-node-offering-id", add_option_dict)





