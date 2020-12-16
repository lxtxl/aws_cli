#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/enable-stage-transition.html
if __name__ == '__main__':
    """
	disable-stage-transition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/disable-stage-transition.html
    """

    parameter_display_string = """
    # pipeline-name : The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.
    # stage-name : The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).
    # transition-type : Specifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage (outbound).
Possible values:

Inbound
Outbound
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("codepipeline", "enable-stage-transition", "pipeline-name", "stage-name", "transition-type", add_option_dict)
