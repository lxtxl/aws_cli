#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-db-revision.html
if __name__ == '__main__':
    """
	describe-cluster-db-revisions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-db-revisions.html
    """

    parameter_display_string = """
    # cluster-identifier : The unique identifier of a cluster whose database revision you want to modify.
Example: examplecluster
    # revision-target : The identifier of the database revision. You can retrieve this value from the response to the  DescribeClusterDbRevisions request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "modify-cluster-db-revision", "cluster-identifier", "revision-target", add_option_dict)
