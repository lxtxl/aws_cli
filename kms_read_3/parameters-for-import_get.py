#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-parameters-for-import.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # key-id : The identifier of the symmetric CMK into which you will import key material. The Origin of the CMK must be EXTERNAL .
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # wrapping-algorithm : The algorithm you will use to encrypt the key material before importing it with  ImportKeyMaterial . For more information, see Encrypt the Key Material in the AWS Key Management Service Developer Guide .
Possible values:

RSAES_PKCS1_V1_5
RSAES_OAEP_SHA_1
RSAES_OAEP_SHA_256
    """

    execute_two_parameter("kms", "get-parameters-for-import", "key-id", "wrapping-algorithm", parameter_display_string)