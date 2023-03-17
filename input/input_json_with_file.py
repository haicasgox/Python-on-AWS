import argparse
import json
from urllib import response
import boto3

parser = argparse.ArgumentParser()
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][1]

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

def main():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__=="__main__":
    main()