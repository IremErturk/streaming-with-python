from utils import read_ccloud_config

TOPIC = 'nyc_rides_avro'
RIDE_SCHEMA_PATH = '../../resources/schemas/ride.avsc'

CLUSTER_PROPERTIES_FILE_PATH = 'resources/client.properties'
CC_CLUSTER_PROPS = read_ccloud_config(CLUSTER_PROPERTIES_FILE_PATH)

SR_PROPERTIES_FILE_PATH = 'resources/schema_registry.properties'
CC_SCHEMA_REGISTRY_CONFIG = read_ccloud_config(SR_PROPERTIES_FILE_PATH)
CC_SCHEMA_REGISTRY_PROPS = {
    'url': CC_SCHEMA_REGISTRY_CONFIG['schema_registry.url'],
    "basic.auth.user.info" : CC_SCHEMA_REGISTRY_CONFIG["sasl.username"]+ ":" +CC_SCHEMA_REGISTRY_CONFIG["sasl.password"]
}

PRODUCER_CONFIG = {
    'cluster_props' : CC_CLUSTER_PROPS,
    'schema_registry_props' : CC_SCHEMA_REGISTRY_PROPS,
    'schema.value': RIDE_SCHEMA_PATH
}
CONSUMER_CONFIG = {
    'cluster_props' : CC_CLUSTER_PROPS,
    'schema_registry_props' : CC_SCHEMA_REGISTRY_PROPS,
    'schema.value': RIDE_SCHEMA_PATH,
}