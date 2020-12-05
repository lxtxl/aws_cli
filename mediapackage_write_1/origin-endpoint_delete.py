#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-origin-endpoint.html
if __name__ == '__main__':
    """
	create-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/create-origin-endpoint.html
	describe-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-origin-endpoint.html
	list-origin-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-origin-endpoints.html
	update-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html
    """

    parameter_display_string = """
    # id : The ID of the OriginEndpoint to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediapackage", "delete-origin-endpoint", "id", add_option_dict)





