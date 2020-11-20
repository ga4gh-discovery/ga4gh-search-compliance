import requests
import yaml
import jsonschema
from ga4gh.search.compliance.exception.test_method_exception import TestMethodException

class SchemaValidator(object):

    def __init__(self, schema_url):
        self.schema_url = schema_url
        self.specification_url = None
        self.schema_component_path = None
        self.specification_dict = None
        self.schema_dict = None
        self.__parse_schema_url()
    
    def load_schema(self):

        # get specification YAML over HTTP
        response = requests.get(self.schema_url)
        if response.status_code != 200:
            raise TestMethodException("Failed to retrieve response schema")

        # load the specifciation as a python dict, 
        # then traverse the specification dict to the specified schema
        self.specification_dict = yaml.safe_load(response.content)
        self.__traverse_specification_to_schema()
    
    def validate_instance(self, instance):
        resolver = jsonschema.RefResolver("", self.specification_dict)
        try:
            jsonschema.validate(instance, self.schema_dict, resolver=resolver)
        except jsonschema.exceptions.ValidationError as e:
            raise TestMethodException("Response did not match expected schema at %s" % self.schema_url)

    def __parse_schema_url(self):
        schema_url_split = self.schema_url.split("#")
        if len(schema_url_split) != 2:
            raise Exception("Invalid schema URL syntax")

        self.specification_url = schema_url_split[0]
        self.schema_component_path = schema_url_split[1].split("/")[1:]
    
    def __traverse_specification_to_schema(self):
        obj = self.specification_dict
        for key in self.schema_component_path:
            obj = obj[key]
        self.schema_dict = obj