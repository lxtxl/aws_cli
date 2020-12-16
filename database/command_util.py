import logging
import sys
import inflect

logging.basicConfig(filename='logging.log', level=logging.INFO)
logger = logging.getLogger(__name__)

engine = inflect.engine()

def get_type(command_name):
    logger.info("get type {}".format(command_name))
    name_array = command_name.split('-')

    if len(name_array) == 1:
        return "single", command_name
    else:
        other_array = name_array[1:]
        type_name = name_array[0]
        last_sentence = name_array[-1]
        other_array[len(other_array)-1] = make_singular(last_sentence)
        sentence = "-".join(other_array)

        if type_name == "list" or type_name == "describe":
            type_name = "list"
        elif other_array[-1] != last_sentence:
            logger.error("plura sentence : {}".format(command_name))
    return type_name, sentence



def make_singular(sentence):
    if sentence == "kinesis":
        return sentence
    single_sentence = engine.singular_noun(sentence)
    if single_sentence == False:
        return sentence
    return single_sentence

def is_many(type):
    if type == "list":
        return 1
    return 0