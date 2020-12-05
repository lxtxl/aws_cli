#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html
if __name__ == '__main__':
    """
	create-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-service.html
	describe-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-services.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-services.html
    """

    parameter_display_string = """
    # service : The name of the service to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "update-service", "service", add_option_dict)





