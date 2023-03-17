#Functions to parse input arguments from CLI
import argparse ## Python built-in argument parser
import boto3
from botocore import translate

#ArgumentParser object holds the information necessary to parse the CLI input to Python data types
parser = argparse.ArgumentParser() 

#Add each of the arguments using parser method: parser.add_argument()

parser.add_argument(
    '--text',
    dest="Text", #It force --text input to be parsed to the required parameter: Text
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters",
    required=True
    )

parser.add_argument(
    '--source-language-code', 
    dest="SourceLanguageCode", #It force --text input to be parsed to the required parameter: SourceLanguageCode
    type=str, 
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
    )

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode", #It force --text input to be parsed to the required parameter: TargetLanguageCode
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
    )

args = parser.parse_args()

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print (response)

def main():
    translate_text(**vars(args))
    

if __name__ == "__main__":
    main()
