#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-qualification-type.html
if __name__ == '__main__':
    """
	delete-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/delete-qualification-type.html
	get-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/get-qualification-type.html
	list-qualification-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-qualification-types.html
	update-qualification-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/update-qualification-type.html
    """

    parameter_display_string = """
    # name : The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.
    # description : A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.
    # qualification-type-status : The initial status of the Qualification type.
Constraints: Valid values are: Active | Inactive
Possible values:

Active
Inactive
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("mturk", "create-qualification-type", "name", "description", "qualification-type-status", add_option_dict)
