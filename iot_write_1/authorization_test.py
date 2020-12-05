#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/test-authorization.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # auth-infos : A list of authorization info objects. Simulating authorization will create a response for each authInfo object in the list.
(structure)

A collection of authorization information.
actionType -> (string)

The type of action for which the principal is being authorized.

resources -> (list)

The resources for which the principal is being authorized to perform the specified action.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "test-authorization", "auth-infos", add_option_dict)





