#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-streaming-configurations.html
if __name__ == '__main__':
    """
	get-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-app-instance-streaming-configurations.html
	put-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-app-instance-streaming-configurations.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the streaming configurations being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-app-instance-streaming-configurations", "app-instance-arn", add_option_dict)





