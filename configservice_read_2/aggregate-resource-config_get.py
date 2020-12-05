#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-resource-config.html
if __name__ == '__main__':
    """
	select-aggregate-resource-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/select-aggregate-resource-config.html
    """

    parameter_display_string = """
    # configuration-aggregator-name : The name of the configuration aggregator.
    # resource-identifier : 
    """

    execute_two_parameter("configservice", "get-aggregate-resource-config", "configuration-aggregator-name", "resource-identifier", parameter_display_string)