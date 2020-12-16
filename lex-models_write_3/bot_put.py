#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot.html
if __name__ == '__main__':
    """
	delete-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-bot.html
	get-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot.html
	get-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bots.html
    """

    parameter_display_string = """
    # name : The name of the bot. The name is not case sensitive.
    # locale : Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot.
The default is en-US .
Possible values:

de-DE
en-AU
en-GB
en-US
es-419
es-ES
es-US
fr-FR
fr-CA
it-IT
    # child-directed | --no-child-directed : For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying true or false in the childDirected field. By specifying true in the childDirected field, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying false in the childDirected field, you confirm that your use of Amazon Lex is not related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the childDirected field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.
If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the Amazon Lex FAQ.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lex-models", "put-bot", "name", "locale", "child-directed | --no-child-directed", add_option_dict)
