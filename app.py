from flask import Flask, render_template, request
from merkle_hellman import encrypt, decrypt , clé_publique
import ast
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']
        seq = [2, 7, 11, 21, 42, 89, 180, 354]
        m = 881
        n = 588
        w= clé_publique(seq,m,n)
        if operation == 'encrypt':
            result = encrypt(text,w)
            action = "Chiffré"
        elif operation == 'decrypt':
            try:
                text_list = ast.literal_eval(text)
                if isinstance(text_list, list):
                    result = decrypt(text_list, seq, m, n)
                else:
                    result = "Format invalide"
            except (ValueError, SyntaxError):
                result = "Format invalide"
            action = "Déchiffré"
        else:
            result = "Opération inconnue"
            action = "Erreur"

        return render_template('index.html', result=result, action=action)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
