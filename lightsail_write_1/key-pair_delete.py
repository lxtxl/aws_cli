#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-key-pair.html
if __name__ == '__main__':
    """
	create-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-key-pair.html
	get-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pair.html
	get-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pairs.html
	import-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/import-key-pair.html
    """

    parameter_display_string = """
    # key-pair-name : The name of the key pair to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-key-pair", "key-pair-name", add_option_dict)





