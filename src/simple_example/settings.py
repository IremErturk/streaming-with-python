def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf

TOPIC = 'nyc_rides'
CLIENT_PROPERTIES_FILE_PATH = 'resources/client.properties'

CONFLUENT_CLOUD_CONFIG = read_ccloud_config(CLIENT_PROPERTIES_FILE_PATH)
