#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transform.html
if __name__ == '__main__':
    """
	create-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-ml-transform.html
	delete-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-ml-transform.html
	get-ml-transforms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-transforms.html
	list-ml-transforms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-ml-transforms.html
	update-ml-transform : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-ml-transform.html
    """

    parameter_display_string = """
    # transform-id : The unique identifier of the transform, generated at the time that the transform was created.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("glue", "get-ml-transform", "transform-id", add_option_dict)