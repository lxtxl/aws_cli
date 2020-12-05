#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secrets.html
if __name__ == '__main__':
    """
	create-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html
	delete-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-secret.html
	describe-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/describe-secret.html
	restore-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/restore-secret.html
	rotate-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/rotate-secret.html
	update-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("secretsmanager", "list-secrets", add_option_dict)