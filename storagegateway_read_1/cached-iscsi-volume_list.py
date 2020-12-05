#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cached-iscsi-volumes.html
if __name__ == '__main__':
    """
	create-cached-iscsi-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-cached-iscsi-volume.html
    """

    parameter_display_string = """
    # volume-arns : An array of strings where each string represents the Amazon Resource Name (ARN) of a cached volume. All of the specified cached volumes must be from the same gateway. Use  ListVolumes to get volume ARNs for a gateway.
(string)
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

    execute_one_parameter("storagegateway", "describe-cached-iscsi-volumes", "volume-arns", add_option_dict)