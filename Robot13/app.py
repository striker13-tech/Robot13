import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="WhiteboardAI", page_icon="✏️", layout="wide")
st.title("✏️ WhiteboardAI")
st.caption("Beautiful Whiteboard Video Generator - Script + Prompt + Natural Voice + Download")

topic = st.text_input("Topic", value="How People Become Rich")
style = st.selectbox("Explain Style", ["For Kids - Simple", "For TikTok - Cool", "For School - Formal"])

a1, a2, a3 = st.columns(3)
with a1:
    gen_script = st.checkbox("Generate SCRIPT?", value=True)
with a2:
    gen_prompt = st.checkbox("Generate PROMPT?", value=False)
with a3:
    gen_video = st.checkbox("Generate VIDEO?", value=True)

b1, b2, b3, b4 = st.columns(4)
with b1:
    voice = st.selectbox("AI Voice", ["Natural - Parang Tao (Best)", "Female - Teacher (Soft)", "Male - Teacher (Deep)", "Kid - Cute", "Slow - Malinaw"])
    pitch = 1.0 if "Natural" in voice else 1.1 if "Female" in voice else 0.9 if "Male" in voice else 1.4 if "Kid" in voice else 0.85
    rate = 0.85 if "Natural" in voice else 0.8 if "Slow" in voice else 0.9
with b2:
    duration = st.slider("Video Time (sec)", 30, 600, 60, 30)
with b3:
    size = st.selectbox("Video Size", ["9:16 TikTok", "16:9 YouTube", "1:1 Facebook"])
    w = 380 if "9:16" in size else 640 if "16:9" in size else 500
with b4:
    quality = st.selectbox("Quality", ["720p HD", "1080p Full HD"])
    scale = 1.5 if "720p" in quality else 2

script_input = st.text_area("Script", height=100, placeholder="Type your script here...")
prompt_input = st.text_area("Prompt", height=60, placeholder="Type your prompt here...")
generate = st.button("GENERATE WHAT I CHOSE!", use_container_width=True, type="primary")

if generate:
    if topic.strip() == "" and (gen_script or gen_prompt or gen_video):
        st.warning("Please type a topic first.")
    else:
        final_script = script_input
        if gen_script:
            final_script = "Today we will talk about " + topic + ". Rich people do not become rich by luck. They become rich by habit. First, they save money before they spend money. Second, they learn every day. Third, they work hard and they do not give up. Fourth, they make their money work for them. Fifth, they help other people. So remember, to become rich, you need discipline, learning, hard work, and patience. You do not need to be born rich. You just need to start today. Thank you for watching."
            st.success("SCRIPT GENERATED:")
            st.code(final_script)
        final_prompt = prompt_input
        if gen_prompt:
            final_prompt = "Whiteboard video about " + topic + ", style " + style + ", hand writing, stickman drawing, clear and fun, " + size + ", " + quality
            st.success("PROMPT GENERATED:")
            st.code(final_prompt)
        if gen_video:
            if not gen_script and script_input.strip() == "":
                st.warning("You chose VIDEO but you have no script.")
            else:
                video_script = final_script if gen_script else script_input
                video_prompt = final_prompt if gen_prompt else prompt_input
                st.markdown("### YOUR VIDEO")
                safe_script = video_script.replace('"', '').replace("'", "").replace("\n", " ")
                safe_prompt = video_prompt.replace('"', '').replace("'", "").replace("\n", " ")
                canvas_w = int(w * scale)
                canvas_h = int(340 * scale)
                html = ""
                html += "<div style='width:" + str(w) + "px; max-width:100%; margin:auto; background:#ffffff; border-radius:20px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.2); font-family:Arial;'>"
                html += "<div style='background:#111; color:#fff; padding:10px; text-align:center; font-weight:bold; font-size:14px;'>WHITEBOARD AI | " + size + " | " + quality + "</div>"
                html += "<canvas id='c' width='" + str(canvas_w) + "' height='" + str(canvas_h) + "' style='width:100%; display:block; background:#fffdf5;'></canvas>"
                html += "<div style='padding:14px; background:#fff;'>"
                html += "<div id='txt' style='font-size:19px; font-weight:700; line-height:1.5; min-height:70px; color:#111;'></div>"
                html += "<div style='display:flex; justify-content:space-between; align-items:center; margin-top:8px;'><div id='hand' style='font-size:38px;'>✍️</div><div style='text-align:right;'><div id='speaking' style='font-weight:bold; font-size:13px; color:#00aa00;'>Ready</div><div id='timer' style='font-weight:bold; font-size:13px;'>0s / " + str(duration) + "s</div></div></div>"
                html += "<div style='display:flex; gap
