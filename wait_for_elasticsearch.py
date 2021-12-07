import os
import structlog
from time import time, sleep
from elasticsearch import Elasticsearch

check_timeout = os.getenv("ELASTICSEARCH_CHECK_TIMEOUT", 60)
check_interval = os.getenv("ELASTICSEARCH_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
ES_HOST = os.getenv("ELASTICSEARCH7_HOSTS", "127.0.0.1")
ES_PORT = os.getenv("ELASTICSEARCH7_PORT", "29200")

start_time = time()
logger = structlog.get_logger(__name__)


def es_isready():
    url = "http://{}:{}/".format(ES_HOST, ES_PORT)
    while time() - start_time < check_timeout:
        es = Elasticsearch([url], verify_certs=False)
        if es.ping():
            es.ping()
            logger.info("ElasticSearch is ready! ✨ 💅")
            return True
        else:
            logger.warning(
                f"ElasticSearch isn't ready ({url}). Waiting for {check_interval} {interval_unit}..."
            )
            sleep(check_interval)

    logger.error(
        f"We could not connect to ElasticSearch within {check_timeout} seconds."
    )
    return False


es_isready()
