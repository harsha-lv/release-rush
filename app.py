APP_NAME = "inventory-api"
API_VERSION = "v2"

def service_info():
    return {
        "name": APP_NAME,
        "version": API_VERSION,
        "health": "ok"
    }
