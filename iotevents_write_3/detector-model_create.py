#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/create-detector-model.html
if __name__ == '__main__':
    """
	delete-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/delete-detector-model.html
	describe-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-detector-model.html
	list-detector-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/list-detector-models.html
	update-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/update-detector-model.html
    """

    parameter_display_string = """
    # detector-model-name : The name of the detector model.
    # detector-model-definition : 
    # role-arn : The ARN of the role that grants permission to AWS IoT Events to perform its operations.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iotevents", "create-detector-model", "detector-model-name", "detector-model-definition", "role-arn", add_option_dict)
