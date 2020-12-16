#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-asset.html
if __name__ == '__main__':
    """
	get-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-asset.html
	update-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-asset.html
    """

    parameter_display_string = """
    # asset-id : The unique identifier for an asset.
    # data-set-id : The unique identifier for a data set.
    # revision-id : The unique identifier for a revision.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dataexchange", "delete-asset", "asset-id", "data-set-id", "revision-id", add_option_dict)
