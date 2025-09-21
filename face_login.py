from flask import Flask, request, jsonify, render_template_string
from deepface import DeepFace
import cv2, os

app = Flask(__name__)
USERS_DIR = "users_faces"
os.makedirs(USERS_DIR, exist_ok=True)

# ---------- CAPTURAR ROSTRO DESDE WEBCAM ----------
def capture_image(filename="capture.jpg"):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        cap.release()
        return filename
    else:
        cap.release()
        return None



# ---------- REGISTRO ----------
@app.route("/register/<username>", methods=["GET"])
def register(username):
    path = os.path.join(USERS_DIR, username)
    os.makedirs(path, exist_ok=True)

    img_path = os.path.join(path, "face.jpg")
    captured = capture_image(img_path)

    if not captured:
        return jsonify({"msg": "Registro cancelado"})

    return jsonify({"msg": f"Usuario {username} registrado"})


# ---------- LOGIN ----------
@app.route("/login/<username>", methods=["GET"])
def login(username):
    ref_path = os.path.join(USERS_DIR, username, "face.jpg")
    if not os.path.exists(ref_path):
        return jsonify({"msg": "Usuario no registrado"})

    temp_path = "temp.jpg"
    captured = capture_image(temp_path)

    if not captured:
        return jsonify({"msg": "Login cancelado"})

    try:
        result = DeepFace.verify(img1_path=temp_path, img2_path=ref_path, enforce_detection=False)
        if result["verified"]:
            return jsonify({"msg": "Acceso concedido", "verified": True})
        else:
            return jsonify({"msg": "Acceso denegado", "verified": False})
    except Exception as e:
        return jsonify({"error": str(e)})


# ---------- INTERFAZ SIMPLE ----------
@app.route("/")
def index():
    return render_template_string("""
    <h2>Sistema de Login Facial</h2>
    <p>Usa las rutas:</p>
    <ul>
      <li>/register/&lt;usuario&gt; → Registrar usuario</li>
      <li>/login/&lt;usuario&gt; → Iniciar sesión</li>
    </ul>
    <p>Ejemplo: <a href="/register/braulio">/register/braulio</a></p>
    """)


if __name__ == "__main__":
    app.run(debug=True)
