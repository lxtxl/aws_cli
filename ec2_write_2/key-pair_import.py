#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-key-pair.html
if __name__ == '__main__':
    """
	create-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html
	delete-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-key-pair.html
	describe-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-key-pairs.html
    """

    parameter_display_string = """
    # key-name : A unique name for the key pair.
    # public-key-material : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "import-key-pair", "key-name", "public-key-material", add_option_dict)
