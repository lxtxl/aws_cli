#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset.html
if __name__ == '__main__':
    """
	associate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/associate-assets.html
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset.html
	delete-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset.html
	describe-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset.html
	disassociate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/disassociate-assets.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-assets.html
    """

    parameter_display_string = """
    # asset-id : The ID of the asset to update.
    # asset-name : A unique, friendly name for the asset.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsitewise", "update-asset", "asset-id", "asset-name", add_option_dict)
