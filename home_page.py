import streamlit as st
import time
# Home Page content
st.title('Welcome to WEQAYA ')
st.image("weqaya.jpg", caption="Understanding your health", use_container_width=True)
text="**About WEQAYA (وقاية)** \n  \n Weqaya is an intelligent healthcare platform designed to help individuals detect chronic diseases early — such as hypertension, diabetes, and stroke — using advanced artificial intelligence. By analyzing user health data, the system provides instant, data-driven predictions and recommendations, aiming to raise awareness and support preventive care.\n\nوقاية هي منصة رعاية صحية ذكية تهدف إلى مساعدة الأفراد على اكتشاف الأمراض المزمنة مبكرًا — مثل ارتفاع ضغط الدم، والسكري، والسكتة الدماغية — باستخدام تقنيات الذكاء الاصطناعي. من خلال تحليل بيانات المستخدم الصحية، تقدم المنصة تنبؤات فورية وتوصيات قائمة على البيانات، بهدف تعزيز الوعي ودعم الوقاية.\n"


def stream_data():
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)



st.write_stream(stream_data)


# Add any other details for your homepage such as:
# - App Instructions
# - About the project
# - Team info
# - Contact details
