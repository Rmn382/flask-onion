from flask import redirect, url_for
from flask_login import login_required

from __init__ import create_app

app = create_app()


@app.route('/')
@login_required
def index():
    return redirect(url_for('home.index'))


if __name__ == '__main__':
    app.run(debug=True)
