#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/put-detector.html
if __name__ == '__main__':
    """
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector.html
	describe-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-detector.html
	get-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detectors.html
    """

    parameter_display_string = """
    # detector-id : The detector ID.
    # event-type-name : The name of the event type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "put-detector", "detector-id", "event-type-name", add_option_dict)
