#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-subnet-cidr-block.html
if __name__ == '__main__':
    """
	associate-subnet-cidr-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-subnet-cidr-block.html
    """

    parameter_display_string = """
    # association-id : The association ID for the CIDR block.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "disassociate-subnet-cidr-block", "association-id", add_option_dict)





