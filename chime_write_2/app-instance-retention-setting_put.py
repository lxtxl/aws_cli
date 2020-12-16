#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-app-instance-retention-settings.html
if __name__ == '__main__':
    """
	get-app-instance-retention-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-app-instance-retention-settings.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the app instance.
    # app-instance-retention-settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "put-app-instance-retention-settings", "app-instance-arn", "app-instance-retention-settings", add_option_dict)
