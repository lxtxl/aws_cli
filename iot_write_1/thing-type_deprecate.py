#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/deprecate-thing-type.html
if __name__ == '__main__':
    """
	create-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html
	delete-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-type.html
	describe-thing-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-type.html
	list-thing-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-types.html
    """

    parameter_display_string = """
    # thing-type-name : The name of the thing type to deprecate.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "deprecate-thing-type", "thing-type-name", add_option_dict)





