#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/revoke-signature.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : ID of the signing job to be revoked.
    # reason : The reason for revoking the signing job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("signer", "revoke-signature", "job-id", "reason", add_option_dict)
