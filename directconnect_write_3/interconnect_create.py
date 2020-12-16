#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-interconnect.html
if __name__ == '__main__':
    """
	delete-interconnect : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-interconnect.html
	describe-interconnects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-interconnects.html
    """

    parameter_display_string = """
    # interconnect-name : The name of the interconnect.
    # bandwidth : The port bandwidth, in Gbps. The possible values are 1 and 10.
    # location : The location of the interconnect.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("directconnect", "create-interconnect", "interconnect-name", "bandwidth", "location", add_option_dict)
