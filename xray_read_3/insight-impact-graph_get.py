#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-insight-impact-graph.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # insight-id : The insightâs unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.
    # start-time : 
    """

    execute_two_parameter("xray", "get-insight-impact-graph", "insight-id", "start-time", parameter_display_string)