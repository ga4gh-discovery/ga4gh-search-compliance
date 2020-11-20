import json
from ga4gh.search.compliance.config.run_config import RunConfig

class Configuration(object):
    """Global singleton holding all program state information"""

    config_file: str
    run_config: RunConfig
    output_dir: str
    serve: bool
    force: bool

    __instance = None
    
    @staticmethod
    def get_instance():
        if Configuration.__instance == None:
            raise Exception("Configuration not yet loaded, use Configuration.load_instance")
        return Configuration.__instance
    
    @staticmethod
    def load_instance(cli_kwargs):
        if Configuration.__instance != None:
            raise Exception("Configuration already loaded, use Configuration.get_instance")
        else:
            configuration = Configuration(cli_kwargs)
            Configuration.__instance = configuration
    
    def __init__(self, cli_kwargs):
        if Configuration.__instance != None:
            raise Exception("Configuration already loaded, use Configuration.get_instance")
        else:
            self.__set_all_props(**cli_kwargs)

    def __set_all_props(self, config_file, output_dir, serve, force):
        self.config_file = config_file
        self.output_dir = output_dir
        self.serve = serve
        self.force = force

        json_fh = open(self.get_config_file(), "r")
        json_dict = json.load(json_fh)
        self.run_config = RunConfig(**json_dict)

    # GETTERS

    def get_config_file(self):
        return self.config_file
    
    def get_run_config(self):
        return self.run_config

    def get_output_dir(self):
        return self.output_dir

    def get_serve(self):
        return self.serve

    def get_force(self):
        return self.force
