#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex.html
if __name__ == '__main__':
    """
	delete-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex.html
	describe-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex.html
	list-multiplexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplexes.html
	start-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-multiplex.html
	stop-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-multiplex.html
	update-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex.html
    """

    parameter_display_string = """
    # availability-zones : Placeholder documentation for __string
    # multiplex-settings : 
    # name : Name of multiplex.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("medialive", "create-multiplex", "availability-zones", "multiplex-settings", "name", add_option_dict)
