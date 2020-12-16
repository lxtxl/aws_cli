#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-classifiers.html
if __name__ == '__main__':
    """
	create-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-classifier.html
	delete-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-classifier.html
	get-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-classifier.html
	update-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-classifier.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("glue", "get-classifiers", add_option_dict)