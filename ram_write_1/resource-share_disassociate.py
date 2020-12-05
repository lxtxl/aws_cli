#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html
if __name__ == '__main__':
    """
	associate-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share.html
	create-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html
	delete-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/delete-resource-share.html
	get-resource-shares : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html
	update-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/update-resource-share.html
    """

    parameter_display_string = """
    # resource-share-arn : The Amazon Resource Name (ARN) of the resource share.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ram", "disassociate-resource-share", "resource-share-arn", add_option_dict)





