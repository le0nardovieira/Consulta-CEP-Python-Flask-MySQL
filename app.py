import requests

from flask import Flask, render_template, request
from banco import salvar_consulta


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":
        cep = request.form.get("cep")

        if not cep:
            return render_template(
                "index.html",
                erro="Digite um CEP."
            )

        cep = cep.strip()
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")

        if len(cep) != 8 or not cep.isdigit():
            return render_template(
                "index.html",
                erro="CEP inválido. Digite 8 números."
            )

        url = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" in dados:
                return render_template(
                    "index.html",
                    erro="CEP não encontrado."
                )

            salvar_consulta(
                dados.get("cep"),
                dados.get("logradouro"),
                dados.get("bairro"),
                dados.get("localidade"),
                dados.get("uf")
            )

            return render_template(
                "index.html",
                dados=dados,
                sucesso="Consulta realizada com sucesso!"
            )

        return render_template(
            "index.html",
            erro=f"Erro na consulta: {resposta.status_code}"
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)