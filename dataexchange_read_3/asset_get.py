#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-asset.html
if __name__ == '__main__':
    """
	delete-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-asset.html
	update-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-asset.html
    """

    parameter_display_string = """
    # asset-id : The unique identifier for an asset.
    # data-set-id : The unique identifier for a data set.
    """

    execute_two_parameter("dataexchange", "get-asset", "asset-id", "data-set-id", parameter_display_string)