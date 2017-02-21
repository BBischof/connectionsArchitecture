from connectors import Connector

class SalesConnector(Connector):
    url = 'salesurl'

    def proc_model(self):
        return 'uses %s version %s and params: %s' % (self.model_data['name'], self.model_data['version'], self.model_data['parameters'][0][0])
