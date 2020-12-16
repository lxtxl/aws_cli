#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-data-set.html
if __name__ == '__main__':
    """
	delete-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-data-set.html
	get-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-data-set.html
	list-data-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-data-sets.html
	update-data-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-data-set.html
    """

    parameter_display_string = """
    # asset-type : The type of file your data is stored in. Currently, the supported asset type is S3_SNAPSHOT.
Possible values:

S3_SNAPSHOT
    # description : A description for the data set. This value can be up to 16,348 characters long.
    # name : The name of the data set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dataexchange", "create-data-set", "asset-type", "description", "name", add_option_dict)
