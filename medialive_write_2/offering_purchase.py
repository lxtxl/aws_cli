#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/purchase-offering.html
if __name__ == '__main__':
    """
	describe-offering : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-offering.html
	list-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-offerings.html
    """

    parameter_display_string = """
    # count : Number of resources
    # offering-id : Offering to purchase, e.g. â87654321â
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("medialive", "purchase-offering", "count", "offering-id", add_option_dict)
