from flask import Flask

from backend.extensions import cors


def create_app(config='backend.settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    load_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    """ Register Blueprints. """
    from .api.get_spatial_data import api_bp
    from .api.get_gene_list import api_gl
    from .api.get_gene_count import api_gc

    API_VERSION_V1 = 1

    app.register_blueprint(
        api_bp,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1
        )
    )

    app.register_blueprint(
        api_gl,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1
        )
    )

    app.register_blueprint(
        api_gc,
        url_prefix='{prefix}/v{version}'.format(
            prefix=app.config['URL_PREFIX'],
            version=API_VERSION_V1
        )
    )


def load_extensions(app):
    cors.init_app(app, supports_credentials=True, resources=r'/api/*')
    return None
