from flask import Flask, request, jsonify
import pyodbc
import traceback

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-9EJPRQM\\SQLEXPRESS;'
            'DATABASE=NovaAkademi;'
            'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None

@app.route('/add-user', methods=['POST'])
def add_user():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.json
        print(f"Alınan Veri: {data}")

        name = data.get('Name')
        surname = data.get('Surname')

        if name is None or surname is None:
            return jsonify({"error": "Eksik veri: Name ve Surname gerekli."}), 400

        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO dbo.Users (Name, Surname) VALUES (?, ?)",
        (name, surname)
        )
        conn.commit()

        return jsonify({"message": "Kullanıcı başarıyla eklendi"}), 201

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Veritabanı hatası: {str(e)}"}), 500

    finally:
        conn.close()

@app.route('/update-user', methods=['PUT'])
def update_user():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.get_json()
        print(f"Alınan Veri: {data}")

        user_id = data.get('UserID')
        name = data.get('Name')
        surname = data.get('Surname')

        if user_id is None or name is None or surname is None:
            return jsonify({"error": "Eksik veri: UserID, Name ve Surname gerekli."}), 400

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE dbo.Users SET Name = ?, Surname = ? WHERE UserID = ?",
            (name, surname, user_id)
        )
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Kullanıcı bulunamadı"}), 404

        conn.commit()

        return jsonify({"message": "Kullanıcı başarıyla güncellendi"}), 200

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Veritabanı hatası: {str(e)}"}), 500

    finally:
        conn.close()

@app.route('/delete-user', methods=['DELETE'])
def delete_user():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.get_json()
        print(f"Alınan Veri: {data}")

        user_id = data.get('UserID')

        if user_id is None:
            return jsonify({"error": "Eksik veri: UserID gerekli."}), 400

        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM dbo.Users WHERE UserID = ?",
            (user_id,)
        )
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Silinecek kullanıcı bulunamadı"}), 404

        conn.commit()

        return jsonify({"message": "Kullanıcı başarıyla silindi"}), 200

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Veritabanı hatası: {str(e)}"}), 500

    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
