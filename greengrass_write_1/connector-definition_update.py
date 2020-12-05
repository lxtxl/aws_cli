#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/update-connector-definition.html
if __name__ == '__main__':
    """
	create-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-connector-definition.html
	delete-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/delete-connector-definition.html
	get-connector-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-connector-definition.html
	list-connector-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-connector-definitions.html
    """

    parameter_display_string = """
    # connector-definition-id : The ID of the connector definition.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("greengrass", "update-connector-definition", "connector-definition-id", add_option_dict)





