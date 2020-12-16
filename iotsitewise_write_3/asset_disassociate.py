#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/disassociate-assets.html
if __name__ == '__main__':
    """
	associate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/associate-assets.html
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset.html
	delete-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset.html
	describe-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-assets.html
	update-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset.html
    """

    parameter_display_string = """
    # asset-id : The ID of the parent asset from which to disassociate the child asset.
    # hierarchy-id : The ID of a hierarchy in the parent assetâs model. Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see Asset hierarchies in the AWS IoT SiteWise User Guide .
    # child-asset-id : The ID of the child asset to disassociate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iotsitewise", "disassociate-assets", "asset-id", "hierarchy-id", "child-asset-id", add_option_dict)
