#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition-version.html
if __name__ == '__main__':
    """
	get-connector-definition-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition-version.html
	list-connector-definition-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definition-versions.html
    """

    parameter_display_string = """
    # connector-definition-id : The ID of the connector definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "create-connector-definition-version", "connector-definition-id", add_option_dict)





