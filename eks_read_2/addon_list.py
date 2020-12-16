#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-addon.html
if __name__ == '__main__':
    """
	create-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-addon.html
	delete-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-addon.html
	list-addons : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-addons.html
	update-addon : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-addon.html
    """

    parameter_display_string = """
    # cluster-name : The name of the cluster.
    # addon-name : The name of the add-on. The name must match one of the names returned by ` ListAddons https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html`__ .
    """

    execute_two_parameter("eks", "describe-addon", "cluster-name", "addon-name", parameter_display_string)