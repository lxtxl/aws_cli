#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-reserved-instances-exchange-quote.html
if __name__ == '__main__':
    """
	get-reserved-instances-exchange-quote : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-reserved-instances-exchange-quote.html
    """

    parameter_display_string = """
    # reserved-instance-ids : The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or higher value.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "accept-reserved-instances-exchange-quote", "reserved-instance-ids", add_option_dict)





