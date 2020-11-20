from ga4gh.search.compliance.config.server_config import ServerConfig

class RunConfig(object):

    def __init__(self, servers):

        self.servers = []
        for server in servers:
            self.servers.append(ServerConfig(**server))

    # GETTERS

    def get_servers(self):
        return self.servers
