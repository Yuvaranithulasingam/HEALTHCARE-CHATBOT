from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", response="")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"].lower()
    response = generate_health_response(user_message)
    return render_template("index.html", response=response)

def generate_health_response(user_message):
    # Comprehensive list of symptoms with responses
    symptoms_responses = {
        "fever": "It seems like you're experiencing a fever. Drink plenty of fluids and rest. If it exceeds 102°F (39°C), consult a doctor.",
        "cough": "A cough may be caused by a cold or allergies. Drink warm fluids. If persistent, see a doctor.",
        "headache": "Headaches can result from stress or dehydration. Drink water and rest. If severe or recurring, consult a physician.",
        "dizziness": "Dizziness could be due to dehydration or low blood sugar. Stay hydrated. Seek help if it persists.",
        "sore throat": "Sore throat? Gargle with saltwater and drink warm fluids. Seek medical attention if it lasts more than a week.",
        "fatigue": "Feeling fatigued? Ensure you are getting enough rest and eating properly. If it persists, a doctor’s visit might help.",
        "nausea": "Nausea can be caused by many factors. Stay hydrated and avoid rich foods. If it persists, consult a healthcare provider.",
        "body ache": "Body aches are common with viral infections or after physical strain. Rest and hydrate. Seek help if it worsens.",
        "chills": "Chills often accompany fever. Stay warm and drink fluids. Consult a doctor if symptoms persist.",
        "vomiting": "Vomiting can lead to dehydration. Drink small sips of water. If severe or prolonged, consult a doctor.",
        "diarrhea": "Diarrhea can be caused by infections or food intolerances. Stay hydrated with electrolyte-rich fluids.",
        "runny nose": "A runny nose is often a sign of a cold or allergies. Rest and stay hydrated.",
        "shortness of breath": "Shortness of breath could be serious. If it worsens or is accompanied by chest pain, seek medical attention immediately.",
        "chest pain": "Chest pain can be a sign of a heart issue. Seek emergency care if it is severe or persistent.",
        "back pain": "Back pain may result from poor posture or physical strain. Apply a heating pad and rest. See a doctor if it persists.",
        "joint pain": "Joint pain could indicate arthritis or injury. Apply ice and rest. Consult a doctor if persistent.",
        "rash": "Rashes could be caused by allergies or infections. Keep the area clean and avoid irritants.",
        "itching": "Itching may be due to allergies or skin conditions. Apply moisturizing lotion or an antihistamine cream.",
        "sweating": "Excessive sweating could indicate fever or stress. Stay hydrated and rest.",
        "blurry vision": "Blurry vision could indicate eye strain or a more serious issue. Rest your eyes and consult an optometrist.",
        "stomach ache": "A stomach ache could be due to indigestion or a viral infection. Drink clear fluids and rest.",
        "constipation": "Constipation can often be relieved by increasing fiber intake and staying hydrated.",
        "heartburn": "Heartburn may be caused by acid reflux. Avoid spicy foods and try an antacid.",
        "insomnia": "Insomnia can be caused by stress or poor sleep habits. Try to create a relaxing bedtime routine.",
        "sneezing": "Sneezing may indicate allergies or a cold. Avoid allergens and rest.",
        "bruising": "Bruising can occur after minor injuries. Apply ice to reduce swelling.",
        "swelling": "Swelling could indicate injury or infection. Rest and elevate the affected area.",
        "bleeding": "Bleeding may require medical attention depending on severity. Apply pressure to the wound and keep it clean.",
        "palpitations": "Heart palpitations could be caused by stress or caffeine. If they persist or worsen, seek medical advice.",
        "anxiety": "Anxiety can be managed with deep breathing and mindfulness techniques. Seek professional help if it interferes with daily life.",
        "depression": "If you're feeling depressed, it’s important to reach out for support from friends, family, or a healthcare professional.",
        "weight loss": "Unexplained weight loss could be a sign of a medical issue. Consult a doctor for further evaluation.",
        "weight gain": "Weight gain can result from diet or medical conditions. Consider talking to a healthcare provider for advice.",
        "loss of appetite": "Loss of appetite can be caused by stress or illness. Stay hydrated and consult a doctor if it persists.",
        "frequent urination": "Frequent urination may indicate a bladder issue. Drink fluids and see a doctor if it persists.",
        "cold": "A cold often presents with symptoms like sneezing, coughing, and runny nose. Rest and stay hydrated.",
        "flu": "Flu symptoms can include high fever, body aches, and fatigue. Consult a doctor for antiviral medications.",
        "hives": "Hives may be an allergic reaction. Avoid known triggers and consider an antihistamine.",
        "numbness": "Numbness could indicate nerve issues. If it occurs suddenly or persists, consult a doctor.",
        "tingling": "Tingling sensations may indicate nerve compression or anxiety. Seek medical attention if it worsens.",
        "mood swings": "Mood swings can be influenced by stress or hormonal changes. Practice self-care and mindfulness.",
        "memory loss": "Memory loss can be concerning. If it’s persistent or worsening, consult a healthcare provider.",
        "night sweats": "Night sweats could indicate infections or hormonal changes. Consult a doctor if they persist.",
        "hair loss": "Hair loss can result from stress, diet, or medical conditions. Consult a dermatologist for advice.",
        "dry skin": "Dry skin may result from low humidity or skin conditions. Use moisturizers regularly.",
        "acne": "Acne can be caused by hormones or skin care products. Maintain a good skin care routine.",
        "puffiness": "Puffiness around the eyes could be due to lack of sleep or allergies. Ensure you’re getting enough rest.",
        "bad breath": "Bad breath may indicate dental issues. Regular brushing and dental check-ups can help.",
        "earache": "Earaches can result from infections or pressure changes. Consult a doctor if it persists.",
        "nosebleed": "Nosebleeds can occur due to dry air or injury. Pinch your nose and lean forward.",
        "throat tightness": "Tightness in the throat may indicate allergies or anxiety. Seek medical advice if it worsens.",
        "tingling in hands": "Tingling in the hands may result from nerve compression. If persistent, consult a doctor.",
        "pounding headache": "A pounding headache may indicate a migraine. Rest in a dark, quiet room and consult a doctor if severe.",
        "red eyes": "Red eyes could be due to allergies or infections. Consult an eye care professional for advice.",
        "ringing in ears": "Tinnitus, or ringing in the ears, can be caused by noise exposure. Consult a doctor if it persists.",
        "muscle cramps": "Muscle cramps can result from dehydration or overuse. Stay hydrated and stretch regularly.",
        "twitching": "Muscle twitching may be due to stress or fatigue. Ensure you are getting enough rest.",
        "chronic fatigue": "Chronic fatigue may require medical evaluation. Keep a diary of your symptoms for your doctor.",
        "hot flashes": "Hot flashes could indicate hormonal changes. Consult a healthcare provider for advice.",
        "sensitivity to light": "Light sensitivity may result from migraines or eye conditions. Consult an eye doctor if it persists.",
        "stiff neck": "A stiff neck could be due to poor posture or muscle strain. Apply heat and rest.",
        "foot pain": "Foot pain may be caused by footwear or overuse. Ensure you are wearing supportive shoes.",
        "toothache": "Toothaches may indicate dental issues. Consult a dentist for evaluation.",
        "sore muscles": "Sore muscles can occur after exercise. Rest and consider gentle stretching.",
        "leg cramps": "Leg cramps may result from dehydration or overuse. Stay hydrated and stretch before bed.",
        "abdominal pain": "Abdominal pain can arise from many causes. If severe or persistent, consult a doctor.",
        "hiccups": "Hiccups are usually harmless. Holding your breath or sipping cold water may help.",
        "dry mouth": "Dry mouth can result from medications or dehydration. Drink plenty of water.",
        "difficulty swallowing": "Difficulty swallowing could indicate a serious condition. Consult a healthcare provider if it persists.",
        "bloating": "Bloating can be caused by diet or digestive issues. Try to avoid gas-producing foods.",
        "sensitivity to cold": "Sensitivity to cold may indicate thyroid issues. Consult a doctor if you have other symptoms.",
        "feeling faint": "Feeling faint may require medical attention. If you experience this, consult a healthcare provider.",
        "heavy periods": "Heavy periods may indicate hormonal issues. Consult a healthcare provider for evaluation.",
        "irregular periods": "Irregular periods can result from stress or hormonal changes. Keep a record for your doctor.",
        "painful periods": "Painful periods may indicate endometriosis. Consult a healthcare provider for advice.",
        "mood changes": "Mood changes can be influenced by stress or hormonal fluctuations. Practice self-care.",
        "chronic cough": "A chronic cough could indicate asthma or allergies. Consult a doctor for evaluation.",
        "swollen lymph nodes": "Swollen lymph nodes may indicate infection. Consult a doctor if they persist.",
        "cold hands and feet": "Cold extremities can be due to poor circulation. Consult a doctor if persistent.",
        "frequent headaches": "Frequent headaches may require medical evaluation. Keep a diary of symptoms for your doctor.",
        "sensitivity to touch": "Sensitivity to touch may indicate nerve issues. Consult a healthcare provider for evaluation.",
        "restlessness": "Restlessness could be due to anxiety or caffeine. Practice relaxation techniques.",
        "nail changes": "Changes in nails can indicate health issues. Consult a dermatologist if you notice significant changes.",
        "skin rash": "Skin rashes can arise from many causes. Keep the area clean and avoid irritants.",
        "dry eyes": "Dry eyes may result from environmental factors. Use lubricating eye drops.",
        "painful urination": "Painful urination could indicate a urinary tract infection. Consult a doctor for evaluation.",
        "joint stiffness": "Joint stiffness can occur with age or inactivity. Regular movement and stretching can help.",
        "sensitivity to sounds": "Sensitivity to sounds may indicate a condition called hyperacusis. Consult a doctor for evaluation.",
        "excessive thirst": "Excessive thirst may indicate diabetes or dehydration. Consult a healthcare provider.",
        "skin peeling": "Skin peeling can occur after sunburn. Keep the area moisturized.",
        "sun sensitivity": "Sun sensitivity may indicate a skin condition. Use sunscreen and consult a dermatologist.",
        "nail fungus": "Nail fungus can be treated with antifungal medications. Consult a doctor for evaluation.",
        "chronic sinusitis": "Chronic sinusitis may require medical intervention. Consult an ENT specialist.",
        "hypersomnia": "Hypersomnia may indicate a sleep disorder. Keep a sleep diary and consult a doctor.",
        "snoring": "Snoring could indicate sleep apnea. Consult a healthcare provider for evaluation.",
        "tiredness after sleep": "Feeling tired after sleep may indicate sleep disorders. Consult a doctor for evaluation.",
        "fainting": "Fainting could indicate a serious issue. Consult a healthcare provider immediately.",
        "frequent infections": "Frequent infections may indicate an underlying issue. Consult a doctor for evaluation."
    }
    
    # Check for symptoms in the user's message and return the corresponding response
    for symptom, response in symptoms_responses.items():
        if symptom in user_message:
            return response

    return "I'm not sure about that symptom. Please consult a healthcare professional for advice."

if __name__ == "__main__":
    app.run(debug=True)
