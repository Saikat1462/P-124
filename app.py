from flask import Flask,jsonify,request

app=Flask(__name__)
tasks=[
    {
    "id":1,
    "name":"Saikat",
    "contact":"2346545646",
    "done":False
    },
    {
    "id":2,
    "name":"Priyanshu",
    "contact":"56434354235",
    "done":False
    }
]
@app.route("/")
def hello_world():
    return "hello"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400
        )
    task={
        "id":tasks[-1]["id"]+1,
        "name":request.json["title"],
        "contact":request.json.get("contact",""),
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Task Added Successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)