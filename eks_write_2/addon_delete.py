#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-addon.html
if __name__ == '__main__':
    """
	create-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-addon.html
	describe-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-addon.html
	list-addons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-addons.html
	update-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-addon.html
    """

    parameter_display_string = """
    # cluster-name : The name of the cluster to delete the add-on from.
    # addon-name : The name of the add-on. The name must match one of the names returned by ` ListAddons https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html`__ .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("eks", "delete-addon", "cluster-name", "addon-name", add_option_dict)
