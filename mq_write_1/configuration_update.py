#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-configuration.html
if __name__ == '__main__':
    """
	create-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-configuration.html
	describe-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-configuration.html
	list-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-configurations.html
    """

    parameter_display_string = """
    # configuration-id : The unique ID that Amazon MQ generates for the configuration.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mq", "update-configuration", "configuration-id", add_option_dict)





