
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/khayabridge", methods=["POST"])
def khayabridge():
    incoming_msg = request.values.get("Body", "").lower().strip()
    resp = MessagingResponse()
    msg = resp.message()

    if "hello" in incoming_msg or "hi" in incoming_msg:
        msg.body("Welcome to KhayaBridge Capital! I’m KhayaBridge Assistant. What would you like to do?\n\n1. Send Money\n2. Fees\n3. Track Transaction\n4. Talk to an Agent")
    elif incoming_msg == "1" or "send money" in incoming_msg:
        msg.body("To start sending money, please send a clear photo of your ID and tell me:\n- Your full name\n- Destination country\n- Amount to send")
    elif incoming_msg == "2" or "fees" in incoming_msg:
        msg.body("Our fees:\n- SA to Zimbabwe: R49.99\n- SA to Malawi: R59.99\nVisit khayabridge.co.za/fees for full details.")
    elif incoming_msg == "3" or "track" in incoming_msg:
        msg.body("Please enter your transaction reference number to check status.\nExample: KBX20399101ZIM")
    elif incoming_msg == "4" or "agent" in incoming_msg:
        msg.body("Connecting you to a live agent... Please wait.")
    else:
        msg.body("Sorry, I didn’t understand that. Please reply with:\n1. Send Money\n2. Fees\n3. Track Transaction\n4. Talk to an Agent")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
