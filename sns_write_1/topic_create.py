#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html
if __name__ == '__main__':
    """
	delete-topic : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-topic.html
	list-topics : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-topics.html
    """

    parameter_display_string = """
    # name : The name of the topic you want to create.
Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.
For a FIFO (first-in-first-out) topic, the name must end with the .fifo suffix.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sns", "create-topic", "name", add_option_dict)





