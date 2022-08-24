from app.app import create_app
from app.setting import ProdConfig, DevConfig, TestConfig


## Init app
CONFIG = DevConfig
app=create_app(CONFIG)


app.run(host='0.0.0.0')