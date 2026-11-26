import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="WhiteboardAI", page_icon="✏️", layout="wide")
st.title("WhiteboardAI - AI Video Generator")
st.caption("Script + Prompt + Voice Sync + Download")

topic = st.text_input("Topic", placeholder="Type your topic here...")
style = st.selectbox("Explain Style", ["For Kids - Simple", "For TikTok - Cool", "For School - Formal"])
st.subheader("What Do You Want To Generate?")
a1, a2, a3 = st.columns(3)
with a1:
    gen_script = st.checkbox("Generate SCRIPT?", value=True)
with a2:
    gen_prompt = st.checkbox("Generate PROMPT?", value=False)
with a3:
    gen_video = st.checkbox("Generate VIDEO?", value=False)
b1, b2, b3, b4 = st.columns(4)
with b1:
    voice = st.selectbox("AI Voice", ["Female - Teacher", "Male - Teacher", "Kid - Cute", "Robot"])
    pitch = 1.2 if "Female" in voice else 0.8 if "Male" in voice else 1.6 if "Kid" in voice else 0.5
    rate = 0.9
with b2:
    duration = st.slider("Video Time (sec)", 30, 600, 60, 30)
with b3:
    size = st.selectbox("Video Size", ["9:16 TikTok", "16:9 YouTube", "1:1 Facebook"])
    w = 360 if "9:16" in size else 640 if "16:9" in size else 500
with b4:
    quality = st.selectbox("Quality", ["720p HD", "1080p Full HD"])
    scale = 1.5 if "720p" in quality else 2
script_input = st.text_area("Script", height=100, placeholder="Type your script here, or let AI generate it...")
prompt_input = st.text_area("Prompt", height=60, placeholder="Type your prompt here, or let AI generate it...")
generate = st.button("GENERATE WHAT I CHOSE!", use_container_width=True, type="primary")
if generate:
    if topic.strip() == "" and (gen_script or gen_prompt or gen_video):
        st.warning("Please type a topic first.")
    else:
        final_script = script_input
        if gen_script:
            final_script = "Today we will talk about " + topic + ". This is important in our life. First, we need to understand it. Second, we need to do it every day. Third, we need to share it with others. So remember, " + topic + " is very important. Thank you for watching."
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
                canvas_h = int(180 * scale)
                html = ""
                html += "<div style='width:" + str(w) + "px; margin:auto; background:#fff; border:3px solid #333; border-radius:15px; padding:12px;'>"
                html += "<div style='text-align:center; background:#000; color:#fff; padding:5px; border-radius:10px;'>AI VIDEO | " + size + " | " + quality + " | " + str(duration) + "s</div>"
                html += "<div style='font-size:11px; text-align:center;'>Prompt: " + safe_prompt + "</div>"
                html += "<canvas id='c' width='" + str(canvas_w) + "' height='" + str(canvas_h) + "' style='width:100%; border:2px solid #000; background:#fff;'></canvas>"
                html += "<div id='txt' style='font-size:20px; font-weight:bold; min-height:100px;'></div>"
                html += "<div id='hand' style='font-size:40px;'>HAND</div>"
                html += "<div id='speaking' style='text-align:center; font-weight:bold;'>AI is ready...</div>"
                html += "<div id='timer' style='text-align:center;'>0s / " + str(duration) + "s</div>"
                html += "<div style='text-align:center;'><button onclick='startSync()' style='background:#ff0000; color:white; padding:12px 20px; border-radius:25px; font-weight:bold;'>PLAY VIDEO</button>"
                html += "<button onclick='startRecord()' style='background:#333; color:white; padding:12px 20px; border-radius:25px; font-weight:bold; margin-left:8px;'>RECORD + DOWNLOAD</button></div>"
                html += "<a id='dl' style='display:none;'>Download</a></div>"
                html += "<script>"
                html += "var text='" + safe_script + "';"
                html += "var promptText='" + safe_prompt + "';"
                html += "var cv=document.getElementById('c'); var ctx=cv.getContext('2d');"
                html += "var recorder=null; var chunks=[]; var sec=0; var timerInt=null; var words=text.split(' ');"
                html += "var CW=" + str(canvas_w) + "; var CH=" + str(canvas_h) + "; var DUR=" + str(duration) + "; var PITCH=" + str(pitch) + "; var RATE=" + str(rate) + ";"
                html += "function drawBox(){ ctx.fillStyle='#fff'; ctx.fillRect(0,0,CW,CH); ctx.fillStyle='#000'; ctx.font='24px Arial'; ctx.fillText('HOW PEOPLE BECOME RICH',20,40); ctx.font='18px Arial'; ctx.fillText('Whiteboard is Ready!',20,80); ctx.strokeStyle='#000'; ctx.lineWidth=3; ctx.beginPath(); ctx.arc(180,130,16,0,6.3); ctx.stroke(); ctx.beginPath(); ctx.moveTo(180,146); ctx.lineTo(180,190); ctx.stroke(); ctx.fillText('Stickman',100,230); }"
                html += "function drawForWord(word, idx){ ctx.fillStyle='#fff'; ctx.fillRect(0,0,CW,CH); ctx.fillStyle='#000'; ctx.font='20px Arial'; ctx.fillText(word,20,40); ctx.strokeStyle='#000'; ctx.lineWidth=3; ctx.beginPath(); ctx.arc(180,130,16,0,6.3); ctx.stroke(); ctx.beginPath(); ctx.moveTo(180,146); ctx.lineTo(180,190); ctx.stroke(); var low=(word+' '+promptText).toLowerCase(); if(low.indexOf('home')>-1) ctx.fillText('HOME!',20,200); if(low.indexOf('school')>-1) ctx.fillText('SCHOOL!',280,110); if(low.indexOf('rich')>-1) ctx.fillText('RICH!',280,110); if(low.indexOf('money')>-1) ctx.fillText('MONEY!',20,200); var hand=document.getElementById('hand'); hand.style.marginLeft=(idx%8)*30+'px'; }"
                html += "function startSync(){ speechSynthesis.cancel(); document.getElementById('txt').innerHTML=''; document.getElementById('speaking').innerHTML='AI IS SPEAKING...'; drawBox(); var u=new SpeechSynthesisUtterance(text); u.lang='en-US'; u.pitch=PITCH; u.rate=RATE; var wi=0; var fb=setInterval(function(){ if(wi<words.length){ var wd=words[wi]||''; document.getElementById('txt').innerHTML+=wd+' '; drawForWord(wd,wi); wi++; } else { clearInterval(fb); } },600); u.onend=function(){ clearInterval(fb); document.getElementById('speaking').innerHTML='VIDEO DONE!'; }; speechSynthesis.speak(u); sec=0; clearInterval(timerInt); timerInt=setInterval(function(){ sec++; document.getElementById('timer').innerHTML=sec+'s / '+DUR+'s'; if(sec>=DUR) clearInterval(timerInt); },1000); }"
                html += "function startRecord(){ chunks=[]; var stream=cv.captureStream(30); recorder=new MediaRecorder(stream); recorder.ondataavailable=function(e){ if(e.data.size>0) chunks.push(e.data); }; recorder.onstop=function(){ var blob=new Blob(chunks,{type:'video/webm'}); var url=URL.createObjectURL(blob); var a=document.getElementById('dl'); a.href=url; a.download='WhiteboardAI-Video.webm'; a.click(); }; recorder.start(); startSync(); setTimeout(function(){ if(recorder && recorder.state==='recording') recorder.stop(); }, DUR*1000); }"
                html += "drawBox();"
                html += "</script>"
                components.html(html, height=680)
                st.success("VIDEO GENERATED!")
        if not gen_script and not gen_prompt and not gen_video:
            st.warning("Please check at least one.")
