import pywhatkit as kit


def build_alert(category, magnitude, shelter=None):
    if category == "MODERATE_RISK":
        return f"""
⚠️ SEISMOGUARD AI ALERT

Moderate Earthquake Detected

Magnitude: {magnitude:.2f}

Stay Alert.
Emergency teams are monitoring the situation.
"""

    elif category == "HIGH_RISK":
        shelter_name = shelter["name"] if shelter else "N/A"

        return f"""
🚨 SEISMOGUARD AI ALERT

High Risk Earthquake

Magnitude: {magnitude:.2f}

Prepare for evacuation.

Assigned Shelter:
{shelter_name}
"""

    elif category == "EXTREME_RISK":
        shelter_name = shelter["name"] if shelter else "N/A"

        return f"""
🚨🚨 CRITICAL ALERT

Extreme Earthquake Detected

Magnitude: {magnitude:.2f}

Immediate evacuation recommended.

Assigned Shelter:
{shelter_name}
"""

    else:
        return f"""
🌊 TSUNAMI WARNING

Magnitude: {magnitude:.2f}

Move immediately to higher ground.

Follow official evacuation routes.
"""


def send_alert(phone_number, message):
    try:
        kit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            wait_time=15,
            tab_close=True,
            close_time=5,
        )

        return True

    except Exception as e:
        print(e)
        return False
