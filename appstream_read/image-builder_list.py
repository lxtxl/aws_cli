#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-image-builders.html
if __name__ == '__main__':
    """
	create-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-image-builder.html
	delete-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-image-builder.html
	start-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/start-image-builder.html
	stop-image-builder : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-image-builder.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("appstream", "describe-image-builders", add_option_dict)