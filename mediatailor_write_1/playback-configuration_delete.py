#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/delete-playback-configuration.html
if __name__ == '__main__':
    """
	get-playback-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/get-playback-configuration.html
	list-playback-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-playback-configurations.html
	put-playback-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/put-playback-configuration.html
    """

    parameter_display_string = """
    # name : The identifier for the playback configuration.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediatailor", "delete-playback-configuration", "name", add_option_dict)





