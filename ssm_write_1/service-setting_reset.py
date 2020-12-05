#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/reset-service-setting.html
if __name__ == '__main__':
    """
	get-service-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-service-setting.html
	update-service-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-service-setting.html
    """

    parameter_display_string = """
    # setting-id : The Amazon Resource Name (ARN) of the service setting to reset. The setting ID can be /ssm/parameter-store/default-parameter-tier , /ssm/parameter-store/high-throughput-enabled , or /ssm/managed-instance/activation-tier . For example, arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "reset-service-setting", "setting-id", add_option_dict)





