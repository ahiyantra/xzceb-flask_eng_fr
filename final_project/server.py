from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here.
    # implement a method that uses the appropriate translation function through the package you created in the previous part;
    # the function should take the English text as input through the request parameter and return a string
    englishTranslatedToFrench = translator.english_to_french(textToTranslate)
    return englishTranslatedToFrench # "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here.
    # implement a method that uses the appropriate translation function through the package you created in the previous part;
    # the function should take the French text as input through the request parameter and return a string
    frenchTranslatedToEnglish = translator.french_to_english(textToTranslate)
    return frenchTranslatedToEnglish # "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template.
    # implement a method that renders the index[dot]html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
