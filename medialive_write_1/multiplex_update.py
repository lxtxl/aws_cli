#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex.html
if __name__ == '__main__':
    """
	create-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/create-multiplex.html
	delete-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex.html
	describe-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex.html
	list-multiplexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplexes.html
	start-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-multiplex.html
	stop-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-multiplex.html
    """

    parameter_display_string = """
    # multiplex-id : ID of the multiplex to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("medialive", "update-multiplex", "multiplex-id", add_option_dict)





