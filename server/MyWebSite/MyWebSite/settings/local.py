from .common import *

ALLOWED_HOSTS = ["*"]
DEBUG = True
SECRET_KEY = '^r34la!xs$wj=fo_fhv05j=#-q-i-^yegrs89qrk&450gl-ja*'

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "dist/",
        "STATS_FILE": os.path.join(BASE_DIR, "websitefront", "webpack-stats.json"),
    }
}
