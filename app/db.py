import pathlib
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from cassandra.cqlengine import connection

BASE_DIR = pathlib.Path(__file__).resolve().parent

ASTRADB_CONNECT_BUNDLE = BASE_DIR /"connect_bundle"/ "astradb_connect.zip"

ASTRADB_CLIENT_ID = CLIENT_ID
ASTRADB_CLIENT_SECRET = CLIENT_SECRET

def get_session():

  # This secure connect bundle is autogenerated when you download your SCB, 
  # if yours is different update the file name below
  cloud_config= {
    'secure_connect_bundle': CONNECT_BUNDLE
  }

  # This token JSON file is autogenerated when you download your token, 
  # if yours is different update the file name below
  with open("pyakurel.risav@gmail.com-token.json") as f:
      secrets = json.load(f)

  CLIENT_ID = secrets["clientId"]
  CLIENT_SECRET = secrets["secret"]

  auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID,ASTRADB_CLIENT_SECRET )
  cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
  session = cluster.connect()
  connection.register_connection(str(session), session=session)
  connection.set_default_connection(str(session))

  return session