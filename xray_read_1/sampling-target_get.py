#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-targets.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # sampling-statistics-documents : Information about rules that the service is using to sample requests.
(structure)

Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to  GetSamplingTargets .
RuleName -> (string)

The name of the sampling rule.

ClientID -> (string)

A unique identifier for the service in hexadecimal.

Timestamp -> (timestamp)

The current time.

RequestCount -> (integer)

The number of requests that matched the rule.

SampledCount -> (integer)

The number of requests recorded.

BorrowCount -> (integer)

The number of requests recorded with borrowed reservoir quota.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("xray", "get-sampling-targets", "sampling-statistics-documents", add_option_dict)