#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-hosts.html
if __name__ == '__main__':
    """
	allocate-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-hosts.html
	describe-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html
	release-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html
    """

    parameter_display_string = """
    # host-ids : The IDs of the Dedicated Hosts to modify.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-hosts", "host-ids", add_option_dict)





