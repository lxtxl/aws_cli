#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/delete-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/create-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/update-application.html
    """

    parameter_display_string = """
    # application : The name or ID of the application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicecatalog-appregistry", "delete-application", "application", add_option_dict)





