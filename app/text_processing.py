import re


def preprocess_input(input_text):
    input_text = re.sub(r'\s([?.!,"](?:\s|$))', r'\1', input_text)
    split_text = re.split('([.?!])', input_text)
    if split_text[-1] != '':
        split_text.append('')
    input_text = []

    for i in range(0, len(split_text), 2):
        if split_text[i] != '':
            input_text.append((split_text[i]+split_text[i+1]).lstrip())

    return input_text

def preprocess_output(output_text):
    output_text = re.sub(r'\s([?.!,"](?:\s|$))', r'\1', output_text)
    split_text = re.split('([.?!])\s', output_text)
    output_text = ""
    for i in range(0, len(split_text), 2):
        if split_text[i] != '':
            output_text+=((split_text[i]+split_text[i+1]).capitalize())+" "

    return output_text