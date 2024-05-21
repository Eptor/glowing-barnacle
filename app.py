from flask import Flask, render_template, redirect, request
from util import supabase_client
import os
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def inject_user():
    return dict(current_user=supabase_client.auth.get_user())


@app.route("/")
def index():
    print(supabase_client.auth.get_user())
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"Logging in user {email}...")
        print(f"supabase_client.auth.sign_in_with_password({email}, {password})")
        try:
            supabase_client.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
        except:
            print(f"Failed to log in user {email}!")
            return redirect("/login")

        print(f"User {email} logged in successfully!")
        return redirect("/")

    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        print(request.form)
        email = request.form["email"]
        password = request.form["password"]
        print(f"Registering user {email}...")
        print(email, password)
        supabase_client.auth.sign_up({"email": email, "password": password})
        print(f"User {email} registered successfully!")
        return redirect("/")
    return render_template("register.html")


@app.route("/logout")
def logout():
    print("Logging out user...")
    supabase_client.auth.sign_out()
    return redirect("/")


@app.route("/arjs/<experience_id>")
def arjs(experience_id):
    return render_template("arjs.html", _id=experience_id)


@app.route("/maps")
def maps():
    return render_template("maps.html")


@app.route("/upload_experience", methods=["GET", "POST"])
def upload_experience():
    if supabase_client.auth.get_user() is None:
        return redirect("/login")

    if request.method == "GET":
        return render_template("upload_experience.html")

    if "gltf_file" not in request.files:
        return "No file part", 400

    gltf_file = request.files["gltf_file"]
    if gltf_file.filename == "":
        return "No selected file", 400

    if not gltf_file.filename.endswith(".gltf"):
        return "File must be a .gltf", 400

    experience_name = request.form.get("experience_name")

    # Insertar en la tabla 'experiencias'
    response = (
        supabase_client.table("experiencias")
        .insert(
            {
                "nombre": experience_name,
            }
        )
        .execute()
    )

    experience_id = response.data[0]["id"]
    folder_path = os.path.abspath(os.path.join("static", "models", str(experience_id)))
    print(folder_path)

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, str(experience_id) + ".gltf")
    gltf_file.save(file_path)

    return redirect("/arjs/" + str(experience_id))


@app.route("/experiencias")
def experiencias():
    response = supabase_client.table("experiencias").select("*").execute()
    return render_template("experiencias.html", experiencias=response.data)


@app.route("/encuesta", methods=["GET", "POST"])
def encuesta():
    user_response = supabase_client.auth.get_user()
    if user_response is None:
        return redirect("/login")

    if request.method == "GET":
        return render_template("encuesta.html")

    user_id = user_response.user.id
    puntuacion = request.form.get("puntuacion")
    comentarios = request.form.get("comentarios")

    response = (
        supabase_client.table("encuestas_satisfaccion")
        .insert(
            {
                "user_id": user_id,
                "puntuacion": puntuacion,
                "comentarios": comentarios,
            }
        )
        .execute()
    )

    return "Survey submitted successfully!", 201


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
