#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-vpce-configuration.html
if __name__ == '__main__':
    """
	delete-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-vpce-configuration.html
	get-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-vpce-configuration.html
	list-vpce-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-vpce-configurations.html
	update-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-vpce-configuration.html
    """

    parameter_display_string = """
    # vpce-configuration-name : The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
    # vpce-service-name : The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.
    # service-dns-name : The DNS name of the service running in your VPC that you want Device Farm to test.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("devicefarm", "create-vpce-configuration", "vpce-configuration-name", "vpce-service-name", "service-dns-name", add_option_dict)
