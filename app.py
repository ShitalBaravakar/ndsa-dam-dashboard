from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

file_path = r"D:\Shital Chavan\Dummy Dams.xlsx"
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dam Details</title>

<style>
body { font-family: Arial; margin:0; background:#f2f2f2; }
.header { background:#002e5d; color:white; padding:15px; text-align:center; font-size:20px; }
.card { margin:15px; background:white; padding:15px; border-radius:10px; }
table { width:100%; border-collapse: collapse; }
td { border:1px solid #ddd; padding:10px; }
td:first-child { font-weight:bold; background:#f0f0f0; width:40%; }
</style>

</head>

<body>

<div class="header">NDSA Dam Dashboard</div>

<div class="card">
<table>
{% for k, v in data.items() %}
<tr>
<td>{{k}}</td>
<td>{{v}}</td>
</tr>
{% endfor %}
</table>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return "OK"

@app.route("/dam/<int:id>")
def dam(id):
    row = df.iloc[id].to_dict()

    for k in row:
        if pd.isna(row[k]):
            row[k] = ""

    return render_template_string(HTML, data=row)

app.run(host="0.0.0.0", port=5000)