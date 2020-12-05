#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html
if __name__ == '__main__':
    """
	create-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html
	delete-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html
	get-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html
	list-event-source-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html
    """

    parameter_display_string = """
    # uuid : The identifier of the event source mapping.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lambda", "update-event-source-mapping", "uuid", add_option_dict)





