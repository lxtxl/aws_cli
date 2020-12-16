#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/put-scaling-policy.html
if __name__ == '__main__':
    """
	delete-scaling-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-scaling-policy.html
	describe-scaling-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-scaling-policies.html
    """

    parameter_display_string = """
    # name : A descriptive label that is associated with a scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.
    # fleet-id : A unique identifier for a fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.
    # metric-name : Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see Monitor Amazon GameLift with Amazon CloudWatch .

ActivatingGameSessions â Game sessions in the process of being created.
ActiveGameSessions â Game sessions that are currently running.
ActiveInstances â Fleet instances that are currently running at least one game session.
AvailableGameSessions â Additional game sessions that fleet could host simultaneously, given current capacity.
AvailablePlayerSessions â Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
CurrentPlayerSessions â Player slots in active game sessions that are being used by a player or are reserved for a player.
IdleInstances â Active instances that are currently hosting zero game sessions.
PercentAvailableGameSessions â Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
PercentIdleInstances â Percentage of the total number of active instances that are hosting zero game sessions.
QueueDepth â Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
WaitTime â Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

Possible values:

ActivatingGameSessions
ActiveGameSessions
ActiveInstances
AvailableGameSessions
AvailablePlayerSessions
CurrentPlayerSessions
IdleInstances
PercentAvailableGameSessions
PercentIdleInstances
QueueDepth
WaitTime
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("gamelift", "put-scaling-policy", "name", "fleet-id", "metric-name", add_option_dict)
