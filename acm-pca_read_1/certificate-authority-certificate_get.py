#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-certificate.html
if __name__ == '__main__':
    """
	import-certificate-authority-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html
    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) of your private CA. This is of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 `` .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("acm-pca", "get-certificate-authority-certificate", "certificate-authority-arn", add_option_dict)