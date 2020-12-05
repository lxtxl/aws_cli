#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-alias.html
if __name__ == '__main__':
    """
	delete-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-alias.html
    """

    parameter_display_string = """
    # alias-name : Specifies the alias name. This value must begin with alias/ followed by a name, such as alias/ExampleAlias . The alias name cannot begin with alias/aws/ . The alias/aws/ prefix is reserved for AWS managed CMKs.
    # target-key-id : Identifies the CMK to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kms", "create-alias", "alias-name", "target-key-id", add_option_dict)
