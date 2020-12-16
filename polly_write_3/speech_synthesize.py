#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/synthesize-speech.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # output-format : The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json.
When pcm is used, the content returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.
Possible values:

json
mp3
ogg_vorbis
pcm
    # text : Input text to synthesize. If you specify ssml as the TextType , follow the SSML format for the input text.
    # voice-id : Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the DescribeVoices operation.
Possible values:

Aditi
Amy
Astrid
Bianca
Brian
Camila
Carla
Carmen
Celine
Chantal
Conchita
Cristiano
Dora
Emma
Enrique
Ewa
Filiz
Geraint
Giorgio
Gwyneth
Hans
Ines
Ivy
Jacek
Jan
Joanna
Joey
Justin
Karl
Kendra
Kevin
Kimberly
Lea
Liv
Lotte
Lucia
Lupe
Mads
Maja
Marlene
Mathieu
Matthew
Maxim
Mia
Miguel
Mizuki
Naja
Nicole
Olivia
Penelope
Raveena
Ricardo
Ruben
Russell
Salli
Seoyeon
Takumi
Tatyana
Vicki
Vitoria
Zeina
Zhiyu
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("polly", "synthesize-speech", "output-format", "text", "voice-id", add_option_dict)
