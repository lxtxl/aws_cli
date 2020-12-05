#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-container-service.html
if __name__ == '__main__':
    """
	create-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-container-service.html
	delete-container-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-container-service.html
	get-container-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-services.html
    """

    parameter_display_string = """
    # service-name : The name of the container service to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "update-container-service", "service-name", add_option_dict)





