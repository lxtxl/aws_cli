#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/delete-custom-key-store.html
if __name__ == '__main__':
    """
	connect-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/connect-custom-key-store.html
	create-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-custom-key-store.html
	describe-custom-key-stores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-custom-key-stores.html
	disconnect-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disconnect-custom-key-store.html
	update-custom-key-store : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-custom-key-store.html
    """

    parameter_display_string = """
    # custom-key-store-id : Enter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kms", "delete-custom-key-store", "custom-key-store-id", add_option_dict)





