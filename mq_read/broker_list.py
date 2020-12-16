#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-brokers.html
if __name__ == '__main__':
    """
	create-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html
	delete-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-broker.html
	describe-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html
	reboot-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/reboot-broker.html
	update-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-broker.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("mq", "list-brokers", add_option_dict)