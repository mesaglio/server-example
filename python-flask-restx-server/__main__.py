from __init__ import create_app

app = create_app()


if __name__ == "__main__":  # only in dev
    app.run(host="0.0.0.0", port=8080, debug=True)
