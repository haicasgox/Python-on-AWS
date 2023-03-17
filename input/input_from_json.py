import importlib


import json

json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""
def main():
    json_input = json.loads(json_string)
    json_input = json.dumps(json_input, indent=2)
    print(json_input)
if __name__=="__main__":
    main()