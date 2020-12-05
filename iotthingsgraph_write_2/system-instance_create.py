#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-instance.html
if __name__ == '__main__':
    """
	delete-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-instance.html
	deploy-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deploy-system-instance.html
	get-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-instance.html
	search-system-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-instances.html
	undeploy-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/undeploy-system-instance.html
    """

    parameter_display_string = """
    # definition : 
    # target : The target type of the deployment. Valid values are GREENGRASS and CLOUD .
Possible values:

GREENGRASS
CLOUD
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotthingsgraph", "create-system-instance", "definition", "target", add_option_dict)
