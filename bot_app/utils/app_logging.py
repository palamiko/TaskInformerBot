import logging.config
import logging
import os
import yaml


def setup_logging(default_level, default_path=".\\bot_app\\utils\\log_config.yaml", env_key='LOG_CFG'):
    """
    | **@author:** Prathyush SP
    | Logging Setup
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)

    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')
    print(f'Log level install: {default_level}')
