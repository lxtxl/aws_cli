#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html
if __name__ == '__main__':
    """
	list-signing-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html
	update-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html
	upload-signing-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html
    """

    parameter_display_string = """
    # certificate-id : The ID of the signing certificate to delete.
The format of this parameter, as described by its regex pattern, is a string of characters that can be upper- or lower-cased letters or digits.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-signing-certificate", "certificate-id", add_option_dict)





