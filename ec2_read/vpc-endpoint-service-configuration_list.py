#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-service-configurations.html
if __name__ == '__main__':
    """
	create-vpc-endpoint-service-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-service-configuration.html
	delete-vpc-endpoint-service-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-service-configurations.html
	modify-vpc-endpoint-service-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("ec2", "describe-vpc-endpoint-service-configurations", add_option_dict)