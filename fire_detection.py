import cv2
import numpy as np
from tensorflow.keras.models import load_model
from playsound import playsound
from email_alert import send_email_alert

# 🔁 Add this line at the top
email_sent = False

model = load_model('fire_model.h5')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Frame not captured, skipping...")
        continue

    img = cv2.resize(frame, (64, 64))
    img = np.expand_dims(img, axis=0) / 255.0

    prediction = model.predict(img)[0][0]

    if prediction > 0.98:
        cv2.putText(frame, "FIRE!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if not email_sent:
            playsound("alarm.mp3")
            send_email_alert()
            email_sent = True
    else:
        email_sent = False  # Reset the flag if no fire

    cv2.imshow("Fire Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
