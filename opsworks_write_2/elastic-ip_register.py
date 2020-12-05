#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-elastic-ip.html
if __name__ == '__main__':
    """
	associate-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/associate-elastic-ip.html
	deregister-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-elastic-ip.html
	describe-elastic-ips : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-ips.html
	disassociate-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/disassociate-elastic-ip.html
	update-elastic-ip : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-elastic-ip.html
    """

    parameter_display_string = """
    # elastic-ip : The Elastic IP address.
    # stack-id : The stack ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "register-elastic-ip", "elastic-ip", "stack-id", add_option_dict)
