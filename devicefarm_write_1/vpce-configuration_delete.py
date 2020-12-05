#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-vpce-configuration.html
if __name__ == '__main__':
    """
	create-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-vpce-configuration.html
	get-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-vpce-configuration.html
	list-vpce-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-vpce-configurations.html
	update-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-vpce-configuration.html
    """

    parameter_display_string = """
    # arn : The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("devicefarm", "delete-vpce-configuration", "arn", add_option_dict)





