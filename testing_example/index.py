from flask import Flask, render_template
# from flask_datepicker import datepicker
# Some junk to solve loading module path from parent dir
import sys
import os
spliter = '\\' if os.name == 'nt' else '/'
sys.path.append(
    spliter.join(
        os.getcwd().split(
            spliter
        )[:-1]
    )
)
# End of junk
from flask_fontpicker import fontpicker

app = Flask(__name__, template_folder='.')
l = [
    'https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
    'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
    'https://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js',
    'https://www.jqueryscript.net/demo/Google-Web-Font-Picker-Plugin-With-jQuery-And-jQuery-UI-Webfont-selector/webfont.select.js',
    'https://www.jqueryscript.net/demo/Google-Web-Font-Picker-Plugin-With-jQuery-And-jQuery-UI-Webfont-selector/webfont.select.css'
]
lf = []
for ll in l:
    lf.append('static/' + ll.split('/')[-1:][0])
fontpicker(app, local=lf)


@app.route('/')
def root():
    return render_template('index.html')


app.run(debug=True, port=4000)
