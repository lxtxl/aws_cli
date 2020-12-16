#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-app-instance.html
if __name__ == '__main__':
    """
	create-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance.html
	delete-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance.html
	describe-app-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance.html
	list-app-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instances.html
    """

    parameter_display_string = """
    # app-instance-arn : The ARN of the app instance.
    # name : The name that you want to change.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "update-app-instance", "app-instance-arn", "name", add_option_dict)
