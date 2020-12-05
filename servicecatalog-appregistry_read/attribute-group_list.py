#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-attribute-groups.html
if __name__ == '__main__':
    """
	associate-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/associate-attribute-group.html
	create-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/create-attribute-group.html
	delete-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/delete-attribute-group.html
	disassociate-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/disassociate-attribute-group.html
	get-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-attribute-group.html
	update-attribute-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/update-attribute-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("servicecatalog-appregistry", "list-attribute-groups", add_option_dict)