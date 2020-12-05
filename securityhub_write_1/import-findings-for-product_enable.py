#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-import-findings-for-product.html
if __name__ == '__main__':
    """
	disable-import-findings-for-product : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-import-findings-for-product.html
    """

    parameter_display_string = """
    # product-arn : The ARN of the product to enable the integration for.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("securityhub", "enable-import-findings-for-product", "product-arn", add_option_dict)





