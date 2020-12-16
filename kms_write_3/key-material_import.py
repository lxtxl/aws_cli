#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/import-key-material.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # key-id : The identifier of the symmetric CMK that receives the imported key material. The CMKâs Origin must be EXTERNAL . This must be the same CMK specified in the KeyID parameter of the corresponding  GetParametersForImport request.
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # import-token : 
    # encrypted-key-material : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kms", "import-key-material", "key-id", "import-token", "encrypted-key-material", add_option_dict)
