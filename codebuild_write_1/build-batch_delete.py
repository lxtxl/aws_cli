#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-build-batch.html
if __name__ == '__main__':
    """
	list-build-batches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-build-batches.html
	retry-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/retry-build-batch.html
	start-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build-batch.html
	stop-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html
    """

    parameter_display_string = """
    # id : The identifier of the batch build to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codebuild", "delete-build-batch", "id", add_option_dict)





