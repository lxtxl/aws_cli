#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-connection-notifications.html
if __name__ == '__main__':
    """
	create-vpc-endpoint-connection-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-connection-notification.html
	describe-vpc-endpoint-connection-notifications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connection-notifications.html
	modify-vpc-endpoint-connection-notification : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-connection-notification.html
    """

    parameter_display_string = """
    # connection-notification-ids : One or more notification IDs.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-vpc-endpoint-connection-notifications", "connection-notification-ids", add_option_dict)





