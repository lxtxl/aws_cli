#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule-destination.html
if __name__ == '__main__':
    """
	confirm-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/confirm-topic-rule-destination.html
	delete-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule-destination.html
	get-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule-destination.html
	list-topic-rule-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rule-destinations.html
	update-topic-rule-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-topic-rule-destination.html
    """

    parameter_display_string = """
    # destination-configuration : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "create-topic-rule-destination", "destination-configuration", add_option_dict)





