#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-app-instance-streaming-configurations.html
if __name__ == '__main__':
    """
	delete-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-streaming-configurations.html
	get-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-app-instance-streaming-configurations.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the app instance.
    # app-instance-streaming-configurations : The streaming configurations set for an app instance.
(structure)

The streaming configuration of an app instance.
AppInstanceDataType -> (string)

The data type of the app instance.

ResourceArn -> (string)

The resource ARN.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "put-app-instance-streaming-configurations", "app-instance-arn", "app-instance-streaming-configurations", add_option_dict)
