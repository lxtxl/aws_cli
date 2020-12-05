#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset.html
if __name__ == '__main__':
    """
	associate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/associate-assets.html
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset.html
	delete-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset.html
	disassociate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/disassociate-assets.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-assets.html
	update-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset.html
    """

    parameter_display_string = """
    # asset-id : The ID of the asset.
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

    execute_one_parameter("iotsitewise", "describe-asset", "asset-id", add_option_dict)