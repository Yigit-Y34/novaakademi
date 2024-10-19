'''try:
    with open("veriler.txt","r") as dosya:
        içerik = dosya.read()
except FileNotFoundError:
    print("Dosya Bulunamadı")'''

'''from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime
import traceback

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER= .//SQLEXPRESS;'
            'DATABASE=NovaAkademi;'
            'Trusted_Conection = yes;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Veritabanı bağlatı hatası: {e}")
        return None
    
@app.route('/add-book',methods=['POST'])
def add_book():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error":"Veritabanına bağlanılamadı"}),500
    
    try:
        data = request.json
        print(f"Alınan Veri: {data}")

        yazar_id = data.get)('YazarID')
        baslik = data.get('Başlık')
        yayin_yili_str = data.get('YayınYılı')

    if yazar_id is None or baslik is None or yayin_yili_str is None:
        return jsonify({"error":"Eksik veri: YazarID, Başlık ve Yayın Yılı gerekli."}),400

    try:
     yayin_yili = datetime.strptime(yayin_yili_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error":"Yayın Yılı geçersiz formatta. Format: YYYY-MM-DD."}),400

    cursor = conn.curor()
    cursor.execute(
        "INSERT INTO dbo.Kitaplar (YazarID, Başlık, YayınYılı) VALUES (?,?,?)";
        (yazar_id, baslik , yayin_yili)
    )
    conn.commit()

    return jsonify({"message":"Kitap başarıyla eklendi"}),201'''


from flask import Flask, request, jsonify
import pyodbc
from datetime import datetime
import traceback

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-9EJPRQM\\SQLEXPRESS;'   # Düzgün bir şekilde iki ters eğik çizgi
        'DATABASE=NovaAkademi;'
        'Trusted_Connection=yes;'
)
        return conn
    except pyodbc.Error as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None

@app.route('/add-book', methods=['POST'])
def add_book():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.json
        print(f"Alınan Veri: {data}")

        yazar_id = data.get('YazarID')
        baslik = data.get('Başlık')
        yayin_yili_str = data.get('YayınYılı')

        if yazar_id is None or baslik is None or yayin_yili_str is None:
            return jsonify({"error": "Eksik veri: YazarID, Başlık ve Yayın Yılı gerekli."}), 400

        try:
            yayin_yili = datetime.strptime(yayin_yili_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Yayın Yılı geçersiz formatta. Format: YYYY-MM-DD."}), 400

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dbo.Kitaplar (YazarID, Başlık, YayınYılı) VALUES (?, ?, ?)",
            (yazar_id, baslik, yayin_yili)
        )
        conn.commit()

        return jsonify({"message": "Kitap başarıyla eklendi"}), 201

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": "Veritabanı hatası: {e}"}), 500

    finally:
        conn.close()

@app.route('/update-books', methods=['PUT'])
def update_book():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.get_json()
        print(f"Alınan Veri: {data}")

        yazar_id = data.get('YazarID')
        baslik = data.get('Başlık')
        yayin_yili_str = data.get('YayınYılı')

        if yazar_id is None or baslik is None or yayin_yili_str is None:
            return jsonify({"error": "Eksik veri: YazarID, Başlık ve Yayın Yılı gerekli."}), 400

        try:
            yayin_yili = datetime.strptime(yayin_yili_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Yayın Yılı geçersiz formatta. Format: YYYY-MM-DD."}), 400

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE dbo.Kitaplar SET YazarID = ?, Başlık = ?, YayınYılı = ? ",
            (yazar_id, baslik, yayin_yili)
        )
        if cursor.rowcount == 0:
            return jsonify({"error": "Kitap bulunamadı"}), 404

        conn.commit()

        return jsonify({"message": "Kitap başarıyla güncellendi"}), 200

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Veritabanı hatası: {str(e)}"}), 500

    finally:
        conn.close()

@app.route('/delete-book', methods=['DELETE'])
def delete_book():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Veritabanına bağlanılamadı"}), 500

    try:
        data = request.get_json()
        print(f"Alınan Veri: {data}")

        yazar_id = data.get('YazarID')
        baslik = data.get('Başlık')
        yayin_yili_str = data.get('YayınYılı')

        if yazar_id is None or baslik is None or yayin_yili_str is None:
            return jsonify({"error": "Eksik veri: YazarID, Başlık ve Yayın Yılı gerekli."}), 400

        try:
            yayin_yili = datetime.strptime(yayin_yili_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Yayın Yılı geçersiz formatta. Format: YYYY-MM-DD."}), 400

        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM dbo.Kitaplar WHERE YazarID = ? AND Başlık = ? AND YayınYılı = ?",
            (yazar_id, baslik, yayin_yili)
        )
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Silinecek kitap bulunamadı"}), 404

        conn.commit()

        return jsonify({"message": "Kitap başarıyla silindi"}), 200

    except Exception as e:
        print(f"Hata: {e}")
        print("Traceback:", traceback.format_exc())
        return jsonify({"error": f"Veritabanı hatası: {str(e)}"}), 500

    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
