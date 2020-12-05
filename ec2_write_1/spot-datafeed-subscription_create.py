#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-spot-datafeed-subscription.html
if __name__ == '__main__':
    """
	delete-spot-datafeed-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-spot-datafeed-subscription.html
	describe-spot-datafeed-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html
    """

    parameter_display_string = """
    # bucket : The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, see Rules for bucket naming in the Amazon S3 Developer Guide .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-spot-datafeed-subscription", "bucket", add_option_dict)





