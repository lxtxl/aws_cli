#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-discoverer.html
if __name__ == '__main__':
    """
	create-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/create-discoverer.html
	delete-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-discoverer.html
	describe-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-discoverer.html
	list-discoverers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-discoverers.html
	start-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/start-discoverer.html
	stop-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/stop-discoverer.html
    """

    parameter_display_string = """
    # discoverer-id : The ID of the discoverer.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("schemas", "update-discoverer", "discoverer-id", add_option_dict)





