from flask import Flask

from config import Environemnt, load_config

app = Flask(__name__)

@app.get("/health-check")
def health_check():
    return "Hello World!!"

if __name__ == '__main__':
    config = load_config()
    debug_mode = False if config.ENVIRONMENT == Environemnt.PRODUCTION else True
    print(f"Loading {config.ENVIRONMENT} config values")
    print(f"Debug Mode: {debug_mode}")
    
    app.config["ENVIRONMENT"] = config.ENVIRONMENT
    app.run(host=config.HOST, port=config.PORT, debug=debug_mode)