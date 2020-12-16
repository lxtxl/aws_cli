#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/subscribe.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # s3-bucket : The S3 bucket that the AWS Config delivery channel will use. If the bucket does not exist, it will be automatically created. The value for this argument should follow the form bucket/prefix. Note that the prefix is optional.
    # sns-topic : The SNS topic that the AWS Config delivery channel will use. If the SNS topic does not exist, it will be automatically created. Value for this should be a valid SNS topic name or the ARN of an existing SNS topic.
    # iam-role : The IAM role that the AWS Config configuration recorder will use to record current resource configurations. Value for this should be the ARN of the desired IAM role.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("configservice", "subscribe", "s3-bucket", "sns-topic", "iam-role", add_option_dict)
