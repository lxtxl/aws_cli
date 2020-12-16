#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-template-alias.html
if __name__ == '__main__':
    """
	create-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template-alias.html
	describe-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template-alias.html
	update-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template-alias.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the item to delete.
    # template-id : The ID for the template that the specified alias is for.
    # alias-name : The name for the template alias. To delete a specific alias, you delete the version that the alias points to. You can specify the alias name, or specify the latest version of the template by providing the keyword $LATEST in the AliasName parameter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "delete-template-alias", "aws-account-id", "template-id", "alias-name", add_option_dict)
