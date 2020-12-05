#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service.html
if __name__ == '__main__':
    """
	create-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-service.html
	get-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html
    """

    parameter_display_string = """
    # id : The ID of the service that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicediscovery", "delete-service", "id", add_option_dict)





