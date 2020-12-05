#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html
if __name__ == '__main__':
    """
	create-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html
	delete-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-pipeline.html
	get-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-pipeline.html
	update-image-pipeline : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("imagebuilder", "list-image-pipelines", add_option_dict)