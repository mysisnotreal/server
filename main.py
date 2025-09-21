from flask import Flask, request, jsonify

app = Flask(__name__)

pw = "mys_on_top15"
wh = "https://discord.com/api/webhooks/1417965525606207558/pLs2fW1kWzkBm_Qex7YS6ZTD6TPUBMlWLHiTLNWSTnJWrnDWsSfcQwN5vdeeYQnF26-y"

@app.route("/get-webhook", methods=["GET"])
def get_webhook():
    pw = request.args.get("pw")
    if pw == pw:
        return jsonify({ "webhook": wh })
    else:
        return jsonify({ "error": "Unauthorized" }), 403
