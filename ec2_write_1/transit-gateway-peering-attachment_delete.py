#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-peering-attachment.html
if __name__ == '__main__':
    """
	accept-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-peering-attachment.html
	create-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-peering-attachment.html
	describe-transit-gateway-peering-attachments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-peering-attachments.html
	reject-transit-gateway-peering-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-peering-attachment.html
    """

    parameter_display_string = """
    # transit-gateway-attachment-id : The ID of the transit gateway peering attachment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-transit-gateway-peering-attachment", "transit-gateway-attachment-id", add_option_dict)





