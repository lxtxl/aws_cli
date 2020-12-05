#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-plan.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # mapping : The list of mappings from a source table to target tables.
(structure)

Defines a mapping.
SourceTable -> (string)

The name of the source table.

SourcePath -> (string)

The source path.

SourceType -> (string)

The source type.

TargetTable -> (string)

The target table.

TargetPath -> (string)

The target path.

TargetType -> (string)

The target type.
    # source : 
    """

    execute_two_parameter("glue", "get-plan", "mapping", "source", parameter_display_string)