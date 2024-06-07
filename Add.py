from flask import Flask, request, jsonify

app = Flask(_name_)

# 2. Fonksiyon: Sayının karesini hesaplayan fonksiyon
def calculate_square(number):
    return number ** 2

# 3. Servis: Bu fonksiyonu bir endpoint olarak sunalım
@app.route('/square', methods=['GET'])
def square():
    # İstemciden gelen 'number' parametresini alalım
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({"error": "Lütfen bir sayı parametresi girin"}), 400
    result = calculate_square(number)
    return jsonify({"number": number, "square": result})

if _name_ == '_main_':
    app.run(debug=True)