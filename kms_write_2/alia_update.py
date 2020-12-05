#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-alias.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-alias.html
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-alias.html
    """

    parameter_display_string = """
    # alias-name : Identifies the alias that is changing its CMK. This value must begin with alias/ followed by the alias name, such as alias/ExampleAlias . You cannot use UpdateAlias to change the alias name.
    # target-key-id : Identifies the CMK to associate with the alias. When the update operation completes, the alias will point to this CMK.
The CMK must be in the same AWS account and Region as the alias. Also, the new target CMK must be the same type as the current target CMK (both symmetric or both asymmetric) and they must have the same key usage.
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
To verify that the alias is mapped to the correct CMK, use  ListAliases .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kms", "update-alias", "alias-name", "target-key-id", add_option_dict)
