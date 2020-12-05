#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-vpc-attachment.html
if __name__ == '__main__':
    """
	create-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-vpc-attachment.html
	delete-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-vpc-attachment.html
	describe-transit-gateway-vpc-attachments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-vpc-attachments.html
	modify-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-vpc-attachment.html
	reject-transit-gateway-vpc-attachment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-vpc-attachment.html
    """

    parameter_display_string = """
    # transit-gateway-attachment-id : The ID of the attachment.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "accept-transit-gateway-vpc-attachment", "transit-gateway-attachment-id", add_option_dict)





