import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="WhiteboardAI", page_icon="✏️", layout="wide")
st.title("WhiteboardAI - AI Video Generator")
st.caption("Script + Prompt + Voice Sync + Download | Choose what you want to generate")

topic = st.text_input("Topic", placeholder="Type your topic here...")
style = st.selectbox("Explain Style", ["For Kids - Simple", "For TikTok - Cool", "For School - Formal"])

st.subheader("What Do You Want To Generate?")
c1, c2, c3 = st.columns(3)
with c1:
    gen_script = st.checkbox("Generate SCRIPT?", value=True)
with c2:
    gen_prompt = st.checkbox("Generate PROMPT?", value=False)
with c3:
    gen_video = st.checkbox("Generate VIDEO?", value=False)

c1, c2, c3, c4 = st.columns(4)
with c1:
    voice = st.selectbox("AI Voice", ["Female - Teacher", "Male - Teacher", "Kid - Cute", "Robot"])
    pitch = 1.2 if "Female" in voice else 0.8 if "Male" in voice else 1.6 if "Kid" in voice else 0.5
    rate = 0.9 if "Kid" not in voice else 1.0
with c2:
    duration = st.slider("Video Time (sec)", 30, 600, 60, 30)
    st.write(str(duration) + "s")
with c3:
    size = st.selectbox("Video Size", ["9:16 TikTok", "16:9 YouTube", "1:1 Facebook"])
    w = 360 if "9:16" in size else 640 if "16:9" in size else 500
with c4:
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
                st.warning("You chose VIDEO but you have no script. Please type a script or check Generate SCRIPT.")
            else:
                video_script = final_script if gen_script else script_input
                video_prompt = final_prompt if gen_prompt else prompt_input
                st.markdown("### YOUR VIDEO")
                safe_script = video_script.replace('"', '').replace("'", "").replace("\n", " ")
                safe_prompt = video_prompt.replace('"', '').replace("'", "").replace("\n", " ")
                canvas_w = int(w * scale)
                canvas_h = int(180 * scale)

                # FIXED: No f-triple-quote, use simple string with placeholders
                html_parts = []
                html_parts.append("<div style='width:" + str(w) + "px; max-width:100%; margin:auto; background:#fff; border:3px solid #333; border-radius:15px; padding:12px;'>")
                html_parts.append("<div style='text-align:center; background:#000; color:#fff; padding:5px; border-radius:10px; font-size:12px;'>AI VIDEO | " + size + " | " + quality + " | " + str(duration) + "s | " + voice + "</div>")
                html_parts.append("<div style='font-size:11px; color:#666; text-align:center; margin:5px;'>Prompt: " + safe_prompt + "</div>")
                html_parts.append("<canvas id='c' width='" + str(canvas_w) + "' height='" + str(canvas_h) + "' style='width:100%; border-bottom:2px dashed #aaa;'></canvas>")
                html_parts.append("<div id='txt' style='font-size:20px; font-weight:bold; min-height:110px; font-family:Arial; line-height:1.6;'></div>")
                html_parts.append("<div id='hand' style='font-size:45px;'>Hand</div>")
                html_parts.append("<div id='speaking' style='text-align:center; font-weight:bold; color:green;'>AI is ready...</div>")
                html_parts.append("<div id='timer' style='text-align:center; font-weight:bold;'>0s / " + str(duration) + "s</div>")
                html_parts.append("<div style='text-align:center; margin-top:10px;'>")
                html_parts.append("<button onclick='startSync()' style='background:#ff0000; color:white; border:none; padding:12px 20px; border-radius:25px; font-weight:bold; cursor:pointer;'>PLAY VIDEO</button>")
                html_parts.append("<button onclick='startRecord()' style='background:#333; color:white; border:none; padding:12px 20px; border-radius:25px; font-weight:bold; cursor:pointer; margin-left:8px;'>RECORD + DOWNLOAD</button>")
                html_parts.append("</div><a id='dl' style='display:none;'>Download</a></div>")
                html_parts.append("<script>")
                html_parts.append("var text='" + safe_script + "';")
                html_parts.append("var promptText='" + safe_prompt + "';")
                html_parts.append("var cv=document.getElementById('c'); var ctx=cv.getContext('2d');")
                html_parts.append("var recorder=null; var chunks=[]; var sec=0; var timerInt=null; var words=text.split(' ');")
                html_parts.append("var CW=" + str(canvas_w) + "; var CH=" + str(canvas_h) + "; var DUR=" + str(duration) + "; var PITCH=" + str(pitch) + "; var RATE=" + str(rate) + ";")
                html_parts.append("function drawForWord(word, idx){ ctx.fillStyle='#fff'; ctx.fillRect(0,0,CW,CH); ctx.fillStyle='#000'; ctx.strokeStyle='#000'; ctx.lineWidth=3; ctx.font='20px Arial'; ctx.beginPath(); ctx.arc(CW-50,35,22,0,Math.PI*2); ctx.stroke(); ctx.fillText('Sun',CW-70,42); var x=160+(idx%10)*18; if(x>CW-80) x=CW-80; ctx.beginPath(); ctx.arc(x,65,16,0,Math.PI*2); ctx.stroke(); ctx.beginPath(); ctx.moveTo(x,81); ctx.lineTo(x,125); ctx.stroke(); ctx.beginPath(); ctx.moveTo(x,100); ctx.lineTo(x-20,90); ctx.moveTo(x,100); ctx.lineTo(x+20,90); ctx.stroke(); ctx.beginPath(); ctx.moveTo(x,125); ctx.lineTo(x-16,155); ctx.moveTo(x,125); ctx.lineTo(x+16,155); ctx.stroke(); var low=(word+' '+promptText).toLowerCase(); if(low.indexOf('home')>-1) ctx.fillText('HOME!',20,185); if(low.indexOf('school')>-1) ctx.fillText('SCHOOL!',280,110); if(low.indexOf('family')>-1) ctx.fillText('FAMILY!',20,110); var hand=document.getElementById('hand'); hand.style.marginLeft=(idx%8)*40+'px'; }")
                html_parts.append("function drawInitial(){ ctx.fillStyle='#fff'; ctx.fillRect(0,0,CW,CH); ctx.fillStyle='#000'; ctx.font='24px Arial'; ctx.fillText('HOW PEOPLE BECOME RICH',20,40); ctx.fillText('Whiteboard is Ready!',20,80); ctx.strokeStyle='#000'; ctx.lineWidth=3; ctx.beginPath(); ctx.arc(CW-50,35,22,0,Math.PI*2); ctx.stroke(); ctx.fillText('Sun',CW-70,42); ctx.beginPath(); ctx.arc(180,120,16,0,Math.PI*2); ctx.stroke(); ctx.beginPath(); ctx.moveTo(180,136); ctx.lineTo(180,180); ctx.stroke(); ctx.fillText('Stickman is here!',100,210); }")
html_parts.append("function startSync(){ speechSynthesis.cancel(); document.getElementById('txt').innerHTML=''; document.getElementById('speaking').innerHTML='AI IS SPEAKING...'; drawInitial(); var u=new SpeechSynthesisUtterance(text); u.lang='en-US'; u.pitch=PITCH; u.rate=RATE; var wordIdx=0; var fallback=setInterval(function(){ if(wordIdx<words.length){ var wd=words[wordIdx]||''; var el=document.getElementById('txt'); var all=text.split(' '); var shown=''; for(var i=0;i<=wordIdx;i++){ if(i===wordIdx) shown+='<span style=\"background:yellow;\">'+all[i]+'</span> '; else shown+=all[i]+' '; } el.innerHTML=shown; drawForWord(wd,wordIdx); wordIdx++; } else { clearInterval(fallback); } }, 600); u.onboundary=function(e){ if(e.name==='word'){ var ci=e.charIndex; var up=text.substring(0,ci); var wc=up.split(' ').length-1; var wd2=words[wc]||''; var el2=document.getElementById('txt'); var all2=text.split(' '); var shown2=''; for(var i=0;i<=wc;i++){ if(i===wc) shown2+='<span style=\"background:yellow;\">'+all2[i]+'</span> '; else shown2+=all2[i]+' '; } el2.innerHTML=shown2; drawForWord(wd2,wc); } }; u.onend=function(){ clearInterval(fallback); document.getElementById('speaking').innerHTML='VIDEO DONE!'; document.getElementById('hand').innerHTML='DONE'; }; speechSynthesis.speak(u); sec=0; clearInterval(timerInt); timerInt=setInterval(function(){ sec++; document.getElementById('timer').innerHTML=sec+'s / '+DUR+'s'; if(sec>=DUR) clearInterval(timerInt); },1000); }")
html_parts.append("setTimeout(function(){ drawInitial(); }, 500);")
                html_parts.append("function startRecord(){ chunks=[]; var stream=cv.captureStream(30); try{ recorder=new MediaRecorder(stream); }catch(e){ recorder=new MediaRecorder(stream); } recorder.ondataavailable=function(e){ if(e.data.size>0) chunks.push(e.data); }; recorder.onstop=function(){ var blob=new Blob(chunks,{type:'video/webm'}); var url=URL.createObjectURL(blob); var a=document.getElementById('dl'); a.href=url; a.download='WhiteboardAI-Video.webm'; a.click(); }; recorder.start(); startSync(); setTimeout(function(){ if(recorder && recorder.state==='recording') recorder.stop(); }, DUR*1000); }")
                html_parts.append("</script>")
                html_final = "".join(html_parts)
                components.html(html_final, height=680)
                st.success("VIDEO GENERATED!")

        if not gen_script and not gen_prompt and not gen_video:
            st.warning("Please check at least one: SCRIPT, PROMPT, or VIDEO.")
