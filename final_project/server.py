from machinetranslation import translator
from flask import Flask, render_template, request
import json
import  machinetranslation
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated=machinetranslation.translator.english_to_french(textToTranslate)
    return translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated=machinetranslation.translator.french_to_english(textToTranslate)
    return translated

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
