# import connectors as cons

def connector(config):
    if config['input']['source'] == 'primary_source':
        from SalesConnector import SalesConnector
        return SalesConnector(config)
    elif config['input']['source'] == 'pot':
        from PotConnector import PotConnector
        return PotConnector(config)



