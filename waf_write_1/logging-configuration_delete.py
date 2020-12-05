#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-logging-configuration.html
if __name__ == '__main__':
    """
	get-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-logging-configuration.html
	list-logging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-logging-configurations.html
	put-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-logging-configuration.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the web ACL from which you want to delete the  LoggingConfiguration .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("waf", "delete-logging-configuration", "resource-arn", add_option_dict)





