#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ebs-default-kms-key-id.html
if __name__ == '__main__':
    """
	get-ebs-default-kms-key-id : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ebs-default-kms-key-id.html
	reset-ebs-default-kms-key-id : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-ebs-default-kms-key-id.html
    """

    parameter_display_string = """
    # kms-key-id : The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for Amazon EBS encryption. If this parameter is not specified, your AWS managed CMK for EBS is used. If KmsKeyId is specified, the encrypted state must be true .
You can specify the CMK using any of the following:

Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.
Key alias. For example, alias/ExampleAlias.
Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.
Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.

AWS authenticates the CMK asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.
Amazon EBS does not support asymmetric CMKs.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-ebs-default-kms-key-id", "kms-key-id", add_option_dict)





