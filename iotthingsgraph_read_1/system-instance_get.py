#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-instance.html
if __name__ == '__main__':
    """
	create-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-instance.html
	delete-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-instance.html
	deploy-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deploy-system-instance.html
	search-system-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-instances.html
	undeploy-system-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/undeploy-system-instance.html
    """

    parameter_display_string = """
    # id : The ID of the system deployment instance. This value is returned by CreateSystemInstance .
The ID should be in the following format.

urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iotthingsgraph", "get-system-instance", "id", add_option_dict)