#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-broker.html
if __name__ == '__main__':
    """
	create-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html
	describe-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html
	list-brokers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-brokers.html
	reboot-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/reboot-broker.html
	update-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-broker.html
    """

    parameter_display_string = """
    # broker-id : The unique ID that Amazon MQ generates for the broker.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mq", "delete-broker", "broker-id", add_option_dict)





