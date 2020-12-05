#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/delete-applications.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/create-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/update-application.html
    """

    parameter_display_string = """
    # configuration-ids : Configuration ID of an application to be deleted.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("discovery", "delete-applications", "configuration-ids", add_option_dict)





