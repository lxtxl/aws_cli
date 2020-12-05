#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-asset.html
if __name__ == '__main__':
    """
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-asset.html
	describe-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-asset.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-assets.html
    """

    parameter_display_string = """
    # id : The ID of the MediaPackage VOD Asset resource to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediapackage-vod", "delete-asset", "id", add_option_dict)





