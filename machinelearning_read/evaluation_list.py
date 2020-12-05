#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-evaluations.html
if __name__ == '__main__':
    """
	create-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-evaluation.html
	delete-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/delete-evaluation.html
	get-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-evaluation.html
	update-evaluation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/update-evaluation.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("machinelearning", "describe-evaluations", add_option_dict)