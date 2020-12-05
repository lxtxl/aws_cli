#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/batch-update-detector.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # detectors : The list of detectors (instances) to update, along with the values to update.
(structure)

Information used to update the detector (instance).
messageId -> (string)

The ID to assign to the detector update "message" . Each "messageId" must be unique within each batch sent.

detectorModelName -> (string)

The name of the detector model that created the detectors (instances).

keyValue -> (string)

The value of the input key attribute (identifying the device or system) that caused the creation of this detector (instance).

state -> (structure)

The new state, variable values, and timer settings of the detector (instance).
stateName -> (string)

The name of the new state of the detector (instance).

variables -> (list)

The new values of the detectorâs variables. Any variable whose value isnât specified is cleared.
(structure)

The new value of the variable.
name -> (string)

The name of the variable.

value -> (string)

The new value of the variable.



timers -> (list)

The new values of the detectorâs timers. Any timer whose value isnât specified is cleared, and its timeout event wonât occur.
(structure)

The new setting of a timer.
name -> (string)

The name of the timer.

seconds -> (integer)

The new setting of the timer (the number of seconds before the timer elapses).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotevents-data", "batch-update-detector", "detectors", add_option_dict)





