#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/set-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # pipeline-id : The ID of the pipeline that contains the objects.
    # object-ids : The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.
(string)
    # status : The status to be set on all the objects specified in objectIds . For components, use PAUSE or RESUME . For instances, use TRY_CANCEL , RERUN , or MARK_FINISHED .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("datapipeline", "set-status", "pipeline-id", "object-ids", "status", add_option_dict)
