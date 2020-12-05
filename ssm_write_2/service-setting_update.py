#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-service-setting.html
if __name__ == '__main__':
    """
	get-service-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-service-setting.html
	reset-service-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/reset-service-setting.html
    """

    parameter_display_string = """
    # setting-id : The Amazon Resource Name (ARN) of the service setting to reset. For example, arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled . The setting ID can be one of the following.

/ssm/parameter-store/default-parameter-tier
/ssm/parameter-store/high-throughput-enabled
/ssm/managed-instance/activation-tier
    # setting-value : The new value to specify for the service setting. For the /ssm/parameter-store/default-parameter-tier setting ID, the setting value can be one of the following.

Standard
Advanced
Intelligent-Tiering

For the /ssm/parameter-store/high-throughput-enabled , and /ssm/managed-instance/activation-tier setting IDs, the setting value can be true or false.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ssm", "update-service-setting", "setting-id", "setting-value", add_option_dict)
