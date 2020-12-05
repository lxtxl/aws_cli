#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-multicast-domain.html
if __name__ == '__main__':
    """
	associate-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-transit-gateway-multicast-domain.html
	delete-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-multicast-domain.html
	describe-transit-gateway-multicast-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-multicast-domains.html
	disassociate-transit-gateway-multicast-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-transit-gateway-multicast-domain.html
    """

    parameter_display_string = """
    # transit-gateway-id : The ID of the transit gateway.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-transit-gateway-multicast-domain", "transit-gateway-id", add_option_dict)





