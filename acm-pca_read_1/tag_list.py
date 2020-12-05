#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-tags.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # certificate-authority-arn : The Amazon Resource Name (ARN) that was returned when you called the CreateCertificateAuthority action. This must be of the form:

``arn:aws:acm-pca:region :account :certificate-authority/12345678-1234-1234-1234-123456789012 ``
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

    execute_one_parameter("acm-pca", "list-tags", "certificate-authority-arn", add_option_dict)