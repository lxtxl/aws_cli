#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/start-stream-encryption.html
if __name__ == '__main__':
    """
	stop-stream-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/stop-stream-encryption.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream for which to start encrypting records.
    # encryption-type : The encryption type to use. The only valid value is KMS .
Possible values:

NONE
KMS
    # key-id : The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by âalias/â.You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis .

Key ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012
Alias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName
Globally unique key ID example: 12345678-1234-1234-1234-123456789012
Alias name example: alias/MyAliasName
Master key owned by Kinesis Data Streams: alias/aws/kinesis
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis", "start-stream-encryption", "stream-name", "encryption-type", "key-id", add_option_dict)
