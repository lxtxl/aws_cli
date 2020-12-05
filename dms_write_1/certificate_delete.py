#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-certificate.html
if __name__ == '__main__':
    """
	describe-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-certificates.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/import-certificate.html
    """

    parameter_display_string = """
    # certificate-arn : The Amazon Resource Name (ARN) of the deleted certificate.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dms", "delete-certificate", "certificate-arn", add_option_dict)





