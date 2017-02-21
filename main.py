import DataSources as ds
import sys, json

def main():
  with open(sys.argv[1]) as conf_data:
    config = json.load(conf_data)

  con = ds.connector(config)
  print con.proc_model()

if __name__ == '__main__':
  main()
