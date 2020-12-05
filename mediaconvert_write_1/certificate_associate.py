#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/associate-certificate.html
if __name__ == '__main__':
    """
	disassociate-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/disassociate-certificate.html
    """

    parameter_display_string = """
    # arn : The ARN of the ACM certificate that you want to associate with your MediaConvert resource.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediaconvert", "associate-certificate", "arn", add_option_dict)





