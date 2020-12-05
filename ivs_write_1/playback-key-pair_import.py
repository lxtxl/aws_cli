#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/import-playback-key-pair.html
if __name__ == '__main__':
    """
	delete-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-key-pair.html
	get-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-key-pair.html
	list-playback-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-key-pairs.html
    """

    parameter_display_string = """
    # public-key-material : The public portion of a customer-generated key pair.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ivs", "import-playback-key-pair", "public-key-material", add_option_dict)





