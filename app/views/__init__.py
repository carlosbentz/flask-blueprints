from flask import Flask


def init_app(app: Flask):
    from .category_view import bp as bp_category_view
    from .task_view import bp as bp_task_view
    from .task_category_view import bp as bp_task_category_view
    from .home_view import bp as bp_home_view

    app.register_blueprint(bp_category_view)
    app.register_blueprint(bp_task_view)
    app.register_blueprint(bp_task_category_view)
    app.register_blueprint(bp_home_view)
