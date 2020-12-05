#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-drt-log-bucket.html
if __name__ == '__main__':
    """
	disassociate-drt-log-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/disassociate-drt-log-bucket.html
    """

    parameter_display_string = """
    # log-bucket : The Amazon S3 bucket that contains your AWS WAF logs.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("shield", "associate-drt-log-bucket", "log-bucket", add_option_dict)





