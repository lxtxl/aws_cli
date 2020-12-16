#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-key-pairs.html
if __name__ == '__main__':
    """
	delete-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-key-pair.html
	get-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-key-pair.html
	import-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/import-playback-key-pair.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ivs", "list-playback-key-pairs", add_option_dict)