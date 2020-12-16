#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-activity-stream.html
if __name__ == '__main__':
    """
	stop-activity-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-activity-stream.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the DB cluster, for example, arn:aws:rds:us-east-1:12345667890:cluster:das-cluster .
    # mode : Specifies the mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.
Possible values:

sync
async
    # kms-key-id : The AWS KMS key identifier for encrypting messages in the database activity stream. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the AWS KMS customer master key (CMK).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("rds", "start-activity-stream", "resource-arn", "mode", "kms-key-id", add_option_dict)
