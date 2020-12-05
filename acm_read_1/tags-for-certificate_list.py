#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-tags-for-certificate.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # certificate-arn : String that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:

arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012

For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
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

    execute_one_parameter("acm", "list-tags-for-certificate", "certificate-arn", add_option_dict)