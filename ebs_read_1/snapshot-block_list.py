#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/list-snapshot-blocks.html
if __name__ == '__main__':
    """
	get-snapshot-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/get-snapshot-block.html
	put-snapshot-block : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/put-snapshot-block.html
    """

    parameter_display_string = """
    # snapshot-id : The ID of the snapshot from which to get block indexes and block tokens.
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

    execute_one_parameter("ebs", "list-snapshot-blocks", "snapshot-id", add_option_dict)