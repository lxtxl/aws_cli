#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-entity-type.html
if __name__ == '__main__':
    """
	delete-entity-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-entity-type.html
	get-entity-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-entity-types.html
    """

    parameter_display_string = """
    # name : The name of the entity type.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("frauddetector", "put-entity-type", "name", add_option_dict)





