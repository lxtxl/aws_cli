#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/create-dataset-group.html
if __name__ == '__main__':
    """
	delete-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/delete-dataset-group.html
	describe-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-group.html
	list-dataset-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-dataset-groups.html
	update-dataset-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/update-dataset-group.html
    """

    parameter_display_string = """
    # dataset-group-name : A name for the dataset group.
    # domain : The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the  CreateDataset operation must match.
The Domain and DatasetType that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the RETAIL domain and TARGET_TIME_SERIES as the DatasetType , Amazon Forecast requires that item_id , timestamp , and demand fields are present in your data. For more information, see  howitworks-datasets-groups .
Possible values:

RETAIL
CUSTOM
INVENTORY_PLANNING
EC2_CAPACITY
WORK_FORCE
WEB_TRAFFIC
METRICS
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("forecast", "create-dataset-group", "dataset-group-name", "domain", add_option_dict)
