"""Deliberately vulnerable demo app — for testing CodeQL alerts ONLY.
Do not deploy. Each handler maps to a known CodeQL security query.
"""
import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # CodeQL: py/command-line-injection  (High)
    return str(os.system("ping -c 1 " + host))


@app.route("/user")
def user():
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # CodeQL: py/sql-injection  (High)
    cur.execute("SELECT * FROM users WHERE id = '" + uid + "'")
    return str(cur.fetchall())


if __name__ == "__main__":
    app.run()
