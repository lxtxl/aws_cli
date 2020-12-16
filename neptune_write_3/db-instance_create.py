#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-db-instance.html
if __name__ == '__main__':
    """
	delete-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-instance.html
	reboot-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reboot-db-instance.html
    """

    parameter_display_string = """
    # db-instance-identifier : The DB instance identifier. This parameter is stored as a lowercase string.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.

Example: mydbinstance
    # db-instance-class : The compute and memory capacity of the DB instance, for example, db.m4.large . Not all DB instance classes are available in all AWS Regions.
    # engine : The name of the database engine to be used for this instance.
Valid Values: neptune
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("neptune", "create-db-instance", "db-instance-identifier", "db-instance-class", "engine", add_option_dict)
