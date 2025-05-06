import streamlit as st
import time
# Home Page content
st.title('Welcome to WEQAYA ')
st.image("https://northeurope1-mediap.svc.ms/transform/thumbnail?provider=spo&farmid=189736&inputFormat=design&cs=NWUyNzk1ZTMtY2U4Yy00Y2ZiLWIzMDItMzVmZTVjZDAxNTk3fFNQTw&docid=https%3A%2F%2Fhome.microsoftpersonalcontent.com%2F_api%2Fv2.0%2Fdrives%2Fb!oFwXgSX3P024CQ4oO-bC5LsWj74Jp4pMsPZd_huzczl481MbWdMXS5cAv8-BwV0E%2Fitems%2F01ZBDE3F4XLOXH22JSUJALWTWL4ZJ6HJHG%3Ftempauth%3Dv1e.eyJzaXRlaWQiOiI4MTE3NWNhMC1mNzI1LTRkM2YtYjgwOS0wZTI4M2JlNmMyZTQiLCJhcHBfZGlzcGxheW5hbWUiOiJEZXNpZ25lciIsImFwcGlkIjoiNWUyNzk1ZTMtY2U4Yy00Y2ZiLWIzMDItMzVmZTVjZDAxNTk3IiwiYXVkIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwL2hvbWUubWljcm9zb2Z0cGVyc29uYWxjb250ZW50LmNvbUA5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJleHAiOiIxNzQ2NTQzNjAwIn0.O8-Bh47LTksVbE9Dh0tMgCP0JFxlP6IsS5XeswLVBAwkj0sdB0_PM2kmIc1xxULQd2Ol9UWmg2EV6SCNlV5bHBVAIFVl5ZX7sLhuV83qXNtPxwf4_DfOPVpcJI3qKseclIqKwgvBEHDx9tihSMRnLlVeyP-X0T26xF9K9kAq7zCnuMhjgk1B-fOEmRqmOgA615GrYBoEy7L-WvceVFtF_FV0smY8x5f16UvYbx1XdRTlNhIIMTW9Y5MotOqUFsuHb_XQ7R2IEMAqiXyAhwT0tFW1hhonqu-1DSguGv3mrs_UfMCpeSIlBpvjDX8-pVaYV3CMSj7OuhfiAbL89vNXSJLiTrpX-A3-HdCM9H3bSd2O5e3BkgpGXeqbvOP-BuDy.zAP7tj6vny2bLjQr8E9SU4y_YO1QxQ48Tfpdm3spja8%26version%3DPublished&width=800&height=800&cb=63877899890", caption="Understanding your health", use_container_width=True)
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
