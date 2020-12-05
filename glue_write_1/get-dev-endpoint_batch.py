#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-get-dev-endpoints.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # dev-endpoint-names : The list of DevEndpoint names, which might be the names returned from the ListDevEndpoint operation.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "batch-get-dev-endpoints", "dev-endpoint-names", add_option_dict)





