#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-datastore.html
if __name__ == '__main__':
    """
	create-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-datastore.html
	delete-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-datastore.html
	describe-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-datastore.html
	list-datastores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-datastores.html
    """

    parameter_display_string = """
    # datastore-name : The name of the data store to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotanalytics", "update-datastore", "datastore-name", add_option_dict)





