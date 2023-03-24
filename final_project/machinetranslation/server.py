from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frText=translator.english_to_french(textToTranslate)
    return "%s is the translated french text" %frText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    enText=translator.french_to_english(textToTranslate)
    return "%s is the translated English Text" %enText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render-template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
