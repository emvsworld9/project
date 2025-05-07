import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

# Title
st.title("Diabetes Risk Prediction App")

# Load the dataset
df = pd.read_csv("diabetes_prediction_dataset.csv")
# Encode categorical variables
label_encoders = {}
for col in ['gender', 'smoking_history']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features and target
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

over = SMOTE(sampling_strategy=0.12)
under = RandomOverSampler(sampling_strategy=0.5)
steps = [('o', over), ('u', under)]
pipeline = Pipeline(steps=steps)
X_resampled, y_resampled = pipeline.fit_resample(X, y)
x_train_ros, x_test_ros, y_train_ros, y_test_ros= train_test_split(X_resampled, y_resampled, test_size = 0.2)


# Train model
model = RandomForestClassifier()
model.fit(x_train_ros, y_train_ros)

# Sidebar form
st.header("Enter patient details")
col1, col2 = st.columns(2)
gender = col1.selectbox("Gender", label_encoders['gender'].classes_,help="Select your gender")
age = col2.slider("**Age**", 10, 100, 20, help="Enter your age.")
hypertension_1 = col1.selectbox("**Do you have hypertension**", ["yes","no"], help="Select that you have hypertension or not")
if hypertension_1 == "yes":
    hypertension=1
else:
    hypertension=0
heart_disease_1 = col1.selectbox("**Do you have Heart Disease**", ["yes","no"], help="Select that you have Heart Disease or not")
if heart_disease_1 == "yes":
    heart_disease=1
else:
    heart_disease=0
smoking = col1.selectbox("Smoking History", label_encoders['smoking_history'].classes_,help="Select your type")
bmi = col2.slider("**BMI**", 10, 60, 15, step=1, help="Insert your BMI")
hba1c = col1.slider("**HbA1c Level**", 2, 20, 8, step=1, help="Insert your HbA1c Level")
glucose = col2.slider("**Blood Glucose Level**", 50, 500, 200, step=1, help="Insert your Blood Glucose Level")


# Prepare input data



input_data= pd.DataFrame([{
        'gender': label_encoders['gender'].transform([gender])[0],
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'smoking_history': label_encoders['smoking_history'].transform([smoking])[0],
        'bmi': bmi,
        'HbA1c_level': hba1c,
        'blood_glucose_level': glucose
    }])
    
result = model.predict(input_data)
neg_perc = model.predict_proba(input_data)[0][0]
pos_perc = model.predict_proba(input_data)[0][1]
    
if result == 1:
    result_text = "**High Risk**: You are at risk for diabetes."
    result_color = "red"
else:
    result_text = "**Low Risk**: You are not at risk for diabetes."
    result_color = "green"

perc = f"{max(neg_perc, pos_perc)*100:.2f}%"

st.write("""
    **Important Reminder**:
    Hypertension is a serious health condition that should not be ignored. Please consult a doctor for a full diagnosis and treatment plan.
""")
start_text = f"""
Based on the inputs, this program estimates that the patient *{result_text}* with a **{perc}** probability.
Please note, this is just an estimation. Consult with your doctor for accurate results. We hope you're always in good health.
"""

st.write("-"*50)
end_text = """
**Important Warning:**

If you have been diagnosed with or suspect hypertension, please take immediate steps to manage your condition:

1. **Relax**: Try to stay calm and practice deep breathing exercises.
2. **Avoid Stimulants**: Limit caffeine, nicotine, and alcohol consumption.
3. **Stay Hydrated**: Drink plenty of water throughout the day.
4. **Monitor Your Blood Pressure**: Keep track of your readings using a monitor.
5. **Eat Healthily**: Prioritize fruits, vegetables, and low-sodium foods.
6. **Seek Medical Attention if Necessary**: If you experience symptoms like chest pain, dizziness, or difficulty breathing, seek medical help immediately.
"""
# Conclusion Text with Delay
def stream_data():
    for word in start_text.split(" "):
        yield word + " "
        time.sleep(0.02)

    if result == 1:
        st.error(f"⚠️ The patient is at risk of diabetes! with {perc}")
        st.image("https://media.mehrnews.com/d/2018/11/05/4/2947868.jpg", width=600)
        for word in end_text.split(" "):
            yield word + " "
            time.sleep(0.02)
    else: 
             st.success(f"✅ The patient is not at risk of diabetes with {perc}.  ")
             st.image("https://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg", width=600)

if st.button("**PREDICT**"):
    st.write_stream(stream_data)
