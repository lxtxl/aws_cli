#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-reserved-instances-listing.html
if __name__ == '__main__':
    """
	create-reserved-instances-listing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-reserved-instances-listing.html
	describe-reserved-instances-listings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances-listings.html
    """

    parameter_display_string = """
    # reserved-instances-listing-id : The ID of the Reserved Instance listing.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "cancel-reserved-instances-listing", "reserved-instances-listing-id", add_option_dict)





