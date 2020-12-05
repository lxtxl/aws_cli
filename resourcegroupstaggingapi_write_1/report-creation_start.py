#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/start-report-creation.html
if __name__ == '__main__':
    """
	describe-report-creation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/describe-report-creation.html
    """

    parameter_display_string = """
    # s3-bucket : The name of the Amazon S3 bucket where the report will be stored; for example:

awsexamplebucket

For more information on S3 bucket requirements, including an example bucket policy, see the example S3 bucket policy on this page.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("resourcegroupstaggingapi", "start-report-creation", "s3-bucket", add_option_dict)





