from flask import render_template, request, jsonify, session, redirect, url_for
from auth import register_user, login_user
from db import get_connection
from tasks import task_queue, start_workers

def register_routes(app):
    start_workers()

    @app.route("/")
    def home():
        return redirect(url_for("login_page"))

    @app.route("/register", methods=["GET", "POST"])
    def register_page():
        if request.method == "POST":
            return register_user()
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login_page():
        if request.method == "POST":
            return login_user()
        return render_template("login.html")

    @app.route("/analyze", methods=["GET", "POST"])
    def analyze_page():
        if "user_id" not in session:
            return redirect(url_for("login_page"))

        if request.method == "POST":
            texto = request.form["texto"]
            user_id = session["user_id"]
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO analisis (user_id, texto) VALUES (?, ?)", (user_id, texto))
            analisis_id = c.lastrowid
            conn.commit()
            conn.close()
            task_queue.put((analisis_id, texto))
            return jsonify({"status": "Texto enviado a análisis"})

        return render_template("analyze.html")

    @app.route("/results")
    def results():
        if "user_id" not in session:
            return jsonify([])
        user_id = session["user_id"]
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT texto, resultado, estado FROM analisis WHERE user_id=? ORDER BY id DESC", (user_id,))
        rows = c.fetchall()
        conn.close()
        data = [{"texto": r["texto"], "resultado": r["resultado"], "estado": r["estado"]} for r in rows]
        return jsonify(data)

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login_page"))
