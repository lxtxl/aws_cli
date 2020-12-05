#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-dataflow-endpoint-group.html
if __name__ == '__main__':
    """
	create-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html
	get-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-dataflow-endpoint-group.html
	list-dataflow-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-dataflow-endpoint-groups.html
    """

    parameter_display_string = """
    # dataflow-endpoint-group-id : UUID of a dataflow endpoint group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("groundstation", "delete-dataflow-endpoint-group", "dataflow-endpoint-group-id", add_option_dict)





