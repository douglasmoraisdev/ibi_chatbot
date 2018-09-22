from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.FileHandler',
        'level': 'DEBUG',
        'formatter': 'default',
        'filename': 'debug.log',
    },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})
