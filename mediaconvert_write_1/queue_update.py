#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html
	get-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-queue.html
	list-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html
    """

    parameter_display_string = """
    # name : The name of the queue that you are modifying.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediaconvert", "update-queue", "name", add_option_dict)





