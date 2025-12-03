from flask import Flask, render_template, request, redirect, url_for, session, flash
from db_connection import get_db_connection
import pymysql
import hashlib
import logging

app = Flask(__name__)
app.secret_key = 'mi_secreto'

# ---------- RUTAS BÁSICAS ----------
@app.route('/')
def home():
    # abre directo el dashboard
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ternero')
def ternero():
    return render_template('ternero.html')

@app.route('/novillo')
def novillo():
    return render_template('novillo.html')

@app.route('/novillito')
def novillito():
    return render_template('novillito.html')

@app.route('/vaquillona')
def vaquillona():
    return render_template('vaquillona.html')

@app.route('/vaca')
def vaca():
    return render_template('vaca.html')

@app.route('/toro')
def toro():
    return render_template('toro.html')



@app.route("/register", methods=['GET'])
def register():

    return render_template("register.html")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    nombre = request.form.get('nombre', '').strip()
    apellido = request.form.get('apellido', '').strip()
    correo = request.form.get('correo', '').strip()
    celular = request.form.get('celular', '').strip()
    horario = request.form.get('horario', '').strip()

    # Validación: ahora también son obligatorios celular y horario
    if not nombre or not apellido or not correo or not celular or not horario:
        flash('Todos los campos son obligatorios', 'error')
        return redirect(url_for('register'))

    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO suscripciones (nombre, apellido, correo, celular, horario)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, apellido, correo, celular, horario))
        conn.commit()
        flash('¡Suscripción registrada!', 'success')
    except pymysql.err.IntegrityError:
        flash('Ese correo ya está suscrito.', 'warning')
    except pymysql.Error as e:
        app.logger.exception("Error de base de datos en /subscribe")
        flash(f'Error de base de datos: {e}', 'error')
    finally:
        try:
            conn.close()
        except Exception:
            pass

    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)



   
