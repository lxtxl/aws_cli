#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-service.html
if __name__ == '__main__':
    """
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/delete-service.html
	describe-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-services.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html
    """

    parameter_display_string = """
    # service-name : The name of your service. Up to 255 letters (uppercase and lowercase), numbers, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecs", "create-service", "service-name", add_option_dict)





