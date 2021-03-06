#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-property.html
if __name__ == '__main__':
    """
	update-asset-property : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-property.html
    """

    parameter_display_string = """
    # asset-id : The ID of the asset.
    # property-id : The ID of the asset property.
    """

    execute_two_parameter("iotsitewise", "describe-asset-property", "asset-id", "property-id", parameter_display_string)