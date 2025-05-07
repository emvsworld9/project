import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sidebar form
st.sidebar.header("Enter patient details")
gender = st.sidebar.selectbox("Gender", label_encoders['gender'].classes_)
age = st.sidebar.slider("Age", 0, 120, 30)
hypertension = st.sidebar.selectbox("Hypertension", [0, 1])
heart_disease = st.sidebar.selectbox("Heart Disease", [0, 1])
smoking = st.sidebar.selectbox("Smoking History", label_encoders['smoking_history'].classes_)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
hba1c = st.sidebar.number_input("HbA1c Level", min_value=2.0, max_value=20.0, value=5.5)
glucose = st.sidebar.number_input("Blood Glucose Level", min_value=50, max_value=500, value=100)

# Prepare input data
if st.sidebar.button("Predict"):
    input_data = pd.DataFrame([{
        'gender': label_encoders['gender'].transform([gender])[0],
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'smoking_history': label_encoders['smoking_history'].transform([smoking])[0],
        'bmi': bmi,
        'HbA1c_level': hba1c,
        'blood_glucose_level': glucose
    }])
    
    prediction = model.predict(input_data)[0]

        st.subheader("Prediction Result")
        if prediction == 0:
            st.success("✅ Low Risk: No signs of diabetes or prediabetes.")
            st.image("https://static.vecteezy.com/system/resources/thumbnails/003/780/944/small_2x/businessman-standing-with-good-health-word-balloon-healthy-lifestyle-concept-vector.jpg", width=600)

        elif prediction == 1:
            st.warning("⚠ Moderate Risk: Prediabetes likely.")
            st.image("https://i.ytimg.com/vi/uKNft5xAk0E/maxresdefault.jpg", width=600)
        else:
            st.error("🚨 High Risk: Diabetes detected.")
            st.image("https://www.shutterstock.com/shutterstock/photos/2392588533/display_1500/stock-vector-diabetes-concept-tiny-characters-with-medical-equipment-blood-glucose-level-test-doctors-check-2392588533.jpg", width=600)


# Visualizations tab (placeholder)
if menu == "📊 Visualizations":
    st.subheader("📊 Health Risk Visualizations")

    @st.cache_resource
    def get_fig_BMI(data):
        fig = px.scatter(data, x='BMI', y='Diabetes_012', trendline="ols",
                        title="Relationship between BMI and Diabetes",
                        color_discrete_sequence=["#ff7f0e"])
        fig.update_layout(title=dict(font=dict(size=20, color='blue'), x=0.5, xanchor='center', pad=dict(t=20)),
                        xaxis_title="BMI ", yaxis_title="Diabetes Risk Probability")
        return fig

    @st.cache_resource
    def get_fig_Age(data):
        fig = px.scatter(data, x='Age', y='Diabetes_012', trendline="ols",
                        title="Relationship between Age and Diabetes",
                        color_discrete_sequence=["#ff7f0e"])
        fig.update_layout(title=dict(font=dict(size=20, color='blue'), x=0.5, xanchor='center', pad=dict(t=20)),
                        xaxis_title="Age", yaxis_title="Diabetes Risk Probability")
        return fig

    @st.cache_resource
    def get_fig_PhysHlth(data):
        fig = px.scatter(data, x='PhysHlth', y='Diabetes_012', trendline="ols",
                        title="Relationship between PhysHlth and Diabetes",
                        color_discrete_sequence=["#ff7f0e"])
        fig.update_layout(title=dict(font=dict(size=20, color='blue'), x=0.5, xanchor='center', pad=dict(t=20)),
                        xaxis_title="Physical Health", yaxis_title="Diabetes Risk Probability")
        return fig
    @st.cache_resource
    def get_fig_GenHlth(data):
        fig = px.scatter(data, x='GenHlth', y='Diabetes_012', trendline="ols",
                        title="Relationship between GenHlth and Diabetes",
                        color_discrete_sequence=["#ff7f0e"])
        fig.update_layout(title=dict(font=dict(size=20, color='blue'), x=0.5, xanchor='center', pad=dict(t=20)),
                        xaxis_title="Genral Health", yaxis_title="Diabetes Risk Probability")
        return fig
    @st.cache_resource
    def get_fig_MentHlth(data):
        fig = px.scatter(data, x='MentHlth', y='Diabetes_012', trendline="ols",
                        title="Relationship between MentHlth and Diabetes",
                        color_discrete_sequence=["#ff7f0e"])
        fig.update_layout(title=dict(font=dict(size=20, color='blue'), x=0.5, xanchor='center', pad=dict(t=20)),
                        xaxis_title="Mental Health", yaxis_title="Diabetes Risk Probability")
        return fig


   
    risk_factor = st.sidebar.selectbox('Select Risk Factor', ['BMI', 'Age','Physical Health', 'Mental Health','Genral Health'])
    con = st.sidebar.button('Confirm')

    if con:
        if risk_factor == 'BMI':
            st.plotly_chart(get_fig_BMI(data), use_container_width=True)
            st.write("As Body Mass Index (BMI) increases, the likelihood of diabetes generally rises.")
        elif risk_factor == 'Age':
            st.plotly_chart(get_fig_Age(data), use_container_width=True)
            st.write("Older age groups show a higher probability of having diabetes or prediabetes.")
        elif risk_factor =='Physical Health':
            st.plotly_chart(get_fig_PhysHlth(data),use_container_width=True)
            st.write(" More days of poor physical health are associated with increased diabetes risk.")
        elif risk_factor =='Mental Health':
            st.plotly_chart(get_fig_MentHlth(data),use_container_width=True)
            st.write(" More days of poor Mental health are associated with increased diabetes risk.")
        else:
            st.plotly_chart(get_fig_GenHlth(data), use_container_width=True)
            st.write("Self-rated general health (on a scale from excellent to poor) strongly correlates with diabetes presence.")
