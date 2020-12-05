#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/create-progress-update-stream.html
if __name__ == '__main__':
    """
	delete-progress-update-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/delete-progress-update-stream.html
	list-progress-update-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-progress-update-streams.html
    """

    parameter_display_string = """
    # progress-update-stream-name : The name of the ProgressUpdateStream. Do not store personal data in this field.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mgh", "create-progress-update-stream", "progress-update-stream-name", add_option_dict)





