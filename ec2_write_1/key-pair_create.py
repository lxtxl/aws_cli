#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html
if __name__ == '__main__':
    """
	delete-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-key-pair.html
	describe-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-key-pairs.html
	import-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-key-pair.html
    """

    parameter_display_string = """
    # key-name : A unique name for the key pair.
Constraints: Up to 255 ASCII characters
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "create-key-pair", "key-name", add_option_dict)





