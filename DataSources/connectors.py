import sqlalchemy as sa

# db = sa.connector()

class Connector(object):
  input_data = {}
  private_data = ''
  model_data = {}

  def __init__(self, config):
    self.input_data = config['input']
    self.model_data = config['model']

  def print_source(self):
    return input_data['source']

  def print_source_type(self):
    return input_data['source_type']

  def read_data(self):
    self.private_data = self.input_data['filename']

  def proc_model(self):
    return self.model_data
