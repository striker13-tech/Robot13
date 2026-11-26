import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="WhiteboardAI", page_icon="✏️", layout="wide")
st.title("WhiteboardAI")
st.caption("Beautiful Whiteboard - No Error Version")

topic = st.text_input("Topic", value="How People Become Rich")
style = st.selectbox("Style", ["For Kids - Simple", "For TikTok - Cool", "For School - Formal"])

a1, a2, a3 = st.columns(3)
with a1:
    gen_script = st.checkbox("Generate SCRIPT?", value=True)
with a2:
    gen_prompt = st.checkbox("Generate PROMPT?", value=False)
with a3:
    gen_video = st.checkbox("Generate VIDEO?", value=True)

b1, b2, b3, b4 = st.columns(4)
with b1:
    voice = st.selectbox("AI Voice", ["Natural - Best", "Female - Soft", "Male - Deep", "Kid - Cute"])
    pitch = 1.0
    if "Female" in voice:
        pitch = 1.1
    if "Male" in voice:
        pitch = 0.9
    if "Kid" in voice:
        pitch = 1.4
    rate = 0.85
with b2:
    duration = st.slider("Video Time (sec)", 30, 600, 60, 30)
with b3:
    size = st.selectbox("Video Size", ["9:16 TikTok", "16:9 YouTube", "1:1 Facebook"])
    w = 380
    if "16:9" in size:
        w = 640
    if "1:1" in size:
        w = 500
with b4:
    quality = st.selectbox("Quality", ["720p HD", "1080p Full HD"])
    scale = 1.5
    if "1080p" in quality:
        scale = 2

script_input = st.text_area("Script", height=100)
prompt_input = st.text_area("Prompt", height=60)
generate = st.button("GENERATE!", use_container_width=True, type="primary")

if generate:
    if topic.strip() == "" and (gen_script or gen_prompt or gen_video):
        st.warning("Please type a topic first.")
    else:
        final_script = script_input
        if gen_script:
            final_script = "Today we will talk about " + topic + ". Rich people do not become rich by luck. They become rich by habit. First, they save money before they spend money. Second, they learn every day. Third, they work hard and they do not give up. Fourth, they make their money work for them. Fifth, they help other people. So remember, to become rich, you need discipline, learning, hard work, and patience. You just need to start today. Thank you for watching."
            st.success("SCRIPT:")
            st.code(final_script)
        final_prompt = prompt_input
        if gen_prompt:
            final_prompt = "Whiteboard video about " + topic + ", style " + style + ", hand writing, stickman, clear and fun, " + size + ", " + quality
            st.success("PROMPT:")
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
                # NO LONG LINES - USE TRIPLE QUOTE
                html_template = """
                <div style='width:WWpx; margin:auto; background:#fff; border-radius:20px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.2);'>
                <div style='background:#111; color:#fff; padding:10px; text-align:center; font-weight:bold;'>
                WHITEBOARD AI
                </div>
                <canvas id='c' width='CW' height='CH' style='width:100%; display:block; background:#fffdf5;'></canvas>
                <div style='padding:14px;'>
                <div id='txt' style='font-size:19px; font-weight:700; min-height:70px;'></div>
                <div style='display:flex; justify-content:space-between;'>
                <div id='hand' style='font-size:38px;'>HAND</div>
                <div style='text-align:right;'>
                <div id='speaking' style='font-weight:bold;'>Ready</div>
                <div id='timer' style='font-weight:bold;'>0s / DURs</div>
                </div>
                </div>
                <div style='display:flex; gap:8px; margin-top:12px;'>
                <button onclick='startSync()' style='flex:1; background:#ff0000; color:white; border:none; padding:13px; border-radius:30px; font-weight:bold;'>PLAY VIDEO</button>
                <button onclick='startRecord()' style='flex:1; background:#111; color:white; border:none; padding:13px; border-radius:30px; font-weight:bold;'>RECORD</button>
                </div>
                </div>
                </div>
                <a id='dl' style='display:none;'>Download</a>
                <script>
                var text = 'SCRIPT_HERE';
                var promptText = 'PROMPT_HERE';
                var cv = document.getElementById('c');
                var ctx = cv.getContext('2d');
                var recorder = null;
                var chunks = [];
                var sec = 0;
                var timerInt = null;
                var words = text.split(' ');
                var CW = CW_NUM;
                var CH = CH_NUM;
                var DUR = DUR_NUM;
                var PITCH = PITCH_NUM;
                var RATE = RATE_NUM;
                function drawScene(word, idx) {
                ctx.fillStyle = '#fffdf5';
                ctx.fillRect(0, 0, CW, CH);
                ctx.fillStyle = '#111';
                ctx.font = 'bold 26px Arial';
                ctx.fillText('How People Become Rich', 24, 38);
                ctx.fillStyle = '#ff6b00';
                ctx.fillRect(24, 52, CW - 48, 4);
                var hx = 70 + (idx % 6) * 50;
                var hy = 150;
                ctx.strokeStyle = '#111';
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.arc(hx, hy, 22, 0, 6.3);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(hx, hy + 22);
                ctx.lineTo(hx, hy + 70);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(hx, hy + 35);
                ctx.lineTo(hx - 28, hy + 55);
                ctx.moveTo(hx, hy + 35);
                ctx.lineTo(hx + 28, hy + 55);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(hx, hy + 70);
                ctx.lineTo(hx - 20, hy + 110);
                ctx.moveTo(hx, hy + 70);
                ctx.lineTo(hx + 20, hy + 110);
                ctx.stroke();
                var low = (word + ' ' + promptText).toLowerCase();
                ctx.font = '48px Arial';
                ctx.fillStyle = '#111';
                ctx.font = 'bold 18px Arial';
                if (low.indexOf('rich') > -1 || low.indexOf('money') > -1) {
                ctx.font = '48px Arial';
                ctx.fillText('MONEY', CW - 140, 190);
                ctx.font = 'bold 18px Arial';
                ctx.fillText('MONEY GROWS!', CW - 170, 230);
                } else if (low.indexOf('save') > -1) {
                ctx.font = '48px Arial';
                ctx.fillText('PIGGY', CW - 140, 190);
                ctx.font = 'bold
