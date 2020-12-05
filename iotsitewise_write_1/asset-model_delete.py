#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset-model.html
if __name__ == '__main__':
    """
	create-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset-model.html
	describe-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html
	list-asset-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-asset-models.html
	update-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-model.html
    """

    parameter_display_string = """
    # asset-model-id : The ID of the asset model to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "delete-asset-model", "asset-model-id", add_option_dict)





