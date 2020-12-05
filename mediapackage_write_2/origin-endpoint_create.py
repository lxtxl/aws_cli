#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/create-origin-endpoint.html
if __name__ == '__main__':
    """
	delete-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-origin-endpoint.html
	describe-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-origin-endpoint.html
	list-origin-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-origin-endpoints.html
	update-origin-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html
    """

    parameter_display_string = """
    # channel-id : The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.
    # id : The ID of the OriginEndpoint. The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediapackage", "create-origin-endpoint", "channel-id", "id", add_option_dict)
