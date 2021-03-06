#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-hapg.html
if __name__ == '__main__':
    """
	delete-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-hapg.html
	describe-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-hapg.html
	list-hapgs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-hapgs.html
	modify-hapg : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/modify-hapg.html
    """

    parameter_display_string = """
    # label : The label of the new high-availability partition group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudhsm", "create-hapg", "label", add_option_dict)





