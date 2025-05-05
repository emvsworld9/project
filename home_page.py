import streamlit as st
import time
# Home Page content
st.title('Welcome to WIQAYA ')
st.image("https://designerapp.officeapps.live.com/designerapp/document.ashx?path=/753b5741-725b-4b0d-b6a5-d05d83c9d3a5/DallEGeneratedImages/dalle-a251614d-02c6-44fb-8979-bbf04666852e0251655853260653139000.jpg&dcHint=FranceCentral&fileToken=8281b8df-a9d7-4f9b-b2f4-d99f81ca1b0e&speCId=b1d44124-910b-4dd3-93be-20e010a97ccf&speType=Image&speIdx=1", caption="Understanding your health", use_container_width=True)
text="**About WIQAYA (وقاية)** \n  \n Wiqaya is an intelligent healthcare platform designed to help individuals detect chronic diseases early — such as hypertension, diabetes, and stroke — using advanced artificial intelligence. By analyzing user health data, the system provides instant, data-driven predictions and recommendations, aiming to raise awareness and support preventive care.\n\nوقاية هي منصة رعاية صحية ذكية تهدف إلى مساعدة الأفراد على اكتشاف الأمراض المزمنة مبكرًا — مثل ارتفاع ضغط الدم، والسكري، والسكتة الدماغية — باستخدام تقنيات الذكاء الاصطناعي. من خلال تحليل بيانات المستخدم الصحية، تقدم المنصة تنبؤات فورية وتوصيات قائمة على البيانات، بهدف تعزيز الوعي ودعم الوقاية.\n"


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