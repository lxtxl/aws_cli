#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container.html
if __name__ == '__main__':
    """
	create-container : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/create-container.html
	describe-container : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-container.html
	list-containers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-containers.html
    """

    parameter_display_string = """
    # container-name : The name of the container to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediastore", "delete-container", "container-name", add_option_dict)





