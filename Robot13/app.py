import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Whiteboard13", page_icon="✏️", layout="wide")
st.title("✏️ Whiteboard13 - AI Video Generator")

# ===== TOPIC =====
st.subheader("🤖 AI Generator")
topic = st.text_input("Topic", placeholder="Type your topic here...")
style = st.selectbox("Explain Style", ["For Kids - Simple", "For TikTok - Cool", "For School - Formal"])

# ===== PAGPIPILIAN - HINDI SABAY! =====
st.subheader("✅ What Do You Want To Generate? Choose Only What You Need!")
c_check1, c_check2, c_check3 = st.columns(3)
with c_check1:
    gen_script = st.checkbox("📝 Generate SCRIPT?", value=True)
with c_check2:
    gen_prompt = st.checkbox("🎬 Generate PROMPT?", value=False)
with c_check3:
    gen_video = st.checkbox("🎥 Generate VIDEO?", value=False)

st.caption("👉 Example: If you want SCRIPT only, check SCRIPT only. If you want VIDEO only, check VIDEO only. You choose!")

# ===== SETTINGS =====
c1, c2, c3, c4 = st.columns(4)
with c1:
    voice = st.selectbox("🎤 AI Voice", ["Female - Teacher", "Male - Teacher", "Kid - Cute", "Robot"])
    pitch = 1.2 if "Female" in voice else 0.8 if "Male" in voice else 1.6 if "Kid" in voice else 0.5
    rate = 0.9 if "Kid" not in voice else 1.0
with c2:
    duration = st.slider("⏱️ Video Time (sec)", 30, 600, 60, 30)
    st.write(f"{duration}s = {duration//60}m {duration%60}s")
with c3:
    size = st.selectbox("📐 Video Size", ["9:16 TikTok", "16:9 YouTube", "1:1 Facebook"])
    w = 360 if "9:16" in size else 640 if "16:9" in size else 500
with c4:
    quality = st.selectbox("🎬 Quality", ["720p HD", "1080p Full HD"])
    scale = 1.5 if "720p" in quality else 2

# ===== MANUAL SCRIPT / PROMPT - Pwede mo din i-type sarili mo =====
st.subheader("✍️ Your Script & Prompt (You Can Edit Or Type Your Own)")
script_input = st.text_area("📝 Script", height=100, placeholder="Type your script here, or let AI generate it...", key="script_box")
prompt_input = st.text_area("🎬 Prompt", height=60, placeholder="Type your prompt here, or let AI generate it...", key="prompt_box")

# ===== GENERATE BUTTON =====
generate = st.button("🤖 GENERATE WHAT I CHOSE!", use_container_width=True, type="primary")

if generate:
    if topic.strip() == "" and (gen_script or gen_prompt or gen_video):
        st.warning("Please type a topic first.")
    else:
        # 1. SCRIPT - Only if checked
        final_script = script_input
        if gen_script:
            final_script = f"Today we will talk about {topic}. This is important in our life. First, we need to understand it. Second, we need to do it every day. Third, we need to share it with others. So remember, {topic} is very important. Thank you for watching."
            st.success(f"📝 **SCRIPT GENERATED:**\n\n{final_script}")
            st.code(final_script, language="text")

        # 2. PROMPT - Only if checked
        final_prompt = prompt_input
        if gen_prompt:
            final_prompt = f"Whiteboard video about {topic}, style {style}, hand writing, stickman drawing, {topic} scene, clear and fun, {size}, {quality}"
            st.success(f"🎬 **PROMPT GENERATED:**\n\n{final_prompt}")
            st.code(final_prompt, language="text")

        # 3. VIDEO - Only if checked! Hindi sabay!
        if gen_video:
            # If user did not check script, use what they typed
            if not gen_script and script_input.strip() == "":
                st.warning("You chose VIDEO but you have no script. Please type a script or check Generate SCRIPT.")
            else:
                video_script = final_script if gen_script else script_input
                video_prompt = final_prompt if gen_prompt else prompt_input
                st.markdown("### 🎬 YOUR VIDEO - Generated From Your Choice!")
                safe_script = video_script.replace('"','').replace("'","").replace("\n"," ")
                safe_prompt = video_prompt.replace('"','').replace("'","").replace("\n"," ")
                canvas_w = int(w * scale)
                canvas_h = int(180 * scale)
                html = f"""
                <div style="width:{w}px; max-width:100%; margin:auto; background:#fff; border:3px solid #333; border-radius:15px; padding:12px;">
                    <div style="text-align:center; background:#000; color:#fff; padding:5px; border-radius:10px; font-size:12px;">🤖 AI VIDEO | {size} | {quality} | {duration}s | {voice}</div>
                    <div style="font-size:11px; color:#666; text-align:center; margin:5px;">Prompt: {safe_prompt}</div>
                    <canvas id="c" width="{canvas_w}" height="{canvas_h}" style="width:100%; border-bottom:2px dashed #aaa;"></canvas>
                    <div id="txt" style="font-size:20px; font-weight:bold; min-height:110px; font-family:'Comic Sans MS',cursive; line-height:1.6;"></div>
                    <div id="hand" style="font-size:45px;">✍️</div>
                    <div id="speaking" style="text-align:center; font-weight:bold; color:green;">🎤 AI is ready...</div>
                    <div id="timer" style="text-align:center; font-weight:bold;">⏱️ 0s / {duration}s</div>
                    <div style="text-align:center; margin-top:10px;">
                        <button onclick="startSync()" style="background:#ff0000; color:white; border:none; padding:12px 20px; border-radius:25px; font-weight:bold; cursor:pointer;">▶️ PLAY VIDEO</button>
                        <button onclick="startRecord()" style="background:#333; color:white; border:none; padding:12px 20px; border-radius:25px; font-weight:bold; cursor:pointer; margin-left:8px;">🔴 RECORD + DOWNLOAD</button>
                    </div>
                    <a id="dl" style="display:none;">Download</a>
                </div>
                <script>
                var text="{safe_script}"; var promptText="{safe_prompt}";
                var cv=document.getElementById("c"); var ctx=cv.getContext("2d");
                var recorder=null; var chunks=[]; var sec=0; var timerInt=null; var words=text.split(" ");
                function drawForWord(word, idx){{
                    ctx.fillStyle="#fff"; ctx.fillRect(0,0,{canvas_w},{canvas_h});
                    ctx.fillStyle="#000"; ctx.strokeStyle="#000"; ctx.lineWidth=3; ctx.font="20px Arial";
                    ctx.beginPath(); ctx.arc({canvas_w-50},35,22,0,Math.PI*2); ctx.stroke(); ctx.fillText("☀️",{canvas_w-70},42);
                    var x=160 + (idx%10)*18; if(x>{canvas_w-80}) x={canvas_w-80};
                    ctx.beginPath(); ctx.arc(x,65,16,0,Math.PI*2); ctx.stroke();
                    ctx.beginPath(); ctx.moveTo(x,81); ctx.lineTo(x,125); ctx.stroke();
                    ctx.beginPath(); ctx.moveTo(x,100); ctx.lineTo(x-20,90); ctx.moveTo(x,100); ctx.lineTo(x+20,90); ctx.stroke();
                    ctx.beginPath(); ctx.moveTo(x,125); ctx.lineTo(x-16,155); ctx.moveTo(x,125); ctx.lineTo(x+16,155); ctx.stroke();
                    ctx.fillText("🧑",150,185);
                    var low=(word+" "+promptText).toLowerCase();
                    if(low.includes("home") || low.includes("house")) ctx.fillText("🏠 HOME!",20,185);
                    if(low.includes("school")) ctx.fillText("🎒 SCHOOL!",280,110);
                    if(low.includes("eat") || low.includes("food")) ctx.fillText("🍚 EATING!",280,140);
                    if(low.includes("family")) ctx.fillText("❤️ FAMILY!",20,110);
                    var hand=document.getElementById("hand"); hand.style.marginLeft=(idx%8)*40+"px"; hand.innerHTML="✍️";
                }}
                function startSync(){{
                    speechSynthesis.cancel(); document.getElementById("txt").innerHTML="";
                    document.getElementById("speaking").innerHTML="🎤 AI IS SPEAKING..."; document.getElementById("speaking").style.color="red";
                    var u=new SpeechSynthesisUtterance(text); u.lang="en-US"; u.pitch={pitch}; u.rate={rate};
                    u.onboundary=function(event){{ if(event.name==="word"){{ var charIndex=event.charIndex; var textUpTo=text.substring(0,charIndex); var wordCount=textUpTo.split(" ").length-1; var word=words[wordCount] || ""; var txtEl=document.getElementById("txt"); var allWords=text.split(" "); var shown=""; for(var i=0;i<=wordCount;i++){{ if(i==wordCount) shown += "<span style='background:yellow; padding:2px; border-radius:5px;'>"+allWords[i]+"</span> "; else shown += allWords[i]+" "; }} txtEl.innerHTML=shown; drawForWord(word, wordCount); }} }};
                    u.onend=function(){{ document.getElementById("speaking").innerHTML="✅ VIDEO DONE!"; document.getElementById("speaking").style.color="green"; document.getElementById("hand").innerHTML="✅"; }};
                    speechSynthesis.speak(u); sec=0; clearInterval(timerInt); timerInt=setInterval(function(){{ sec++; document.getElementById("timer").innerHTML="⏱️ "+sec+"s / {duration}s"; if(sec>={duration}) clearInterval(timerInt); }},1000);
                }}
                function startRecord(){{
                    chunks=[]; var stream=cv.captureStream(30);
                    try{{ recorder=new MediaRecorder(stream, {{mimeType:'video/webm;codecs=vp9'}}); }} catch(e){{ recorder=new MediaRecorder(stream); }}
                    recorder.ondataavailable=function(e){{ if(e.data.size>0) chunks.push(e.data); }};
                    recorder.onstop=function(){{ var blob=new Blob(chunks, {{type:'video/webm'}}); var url=URL.createObjectURL(blob); var a=document.getElementById("dl"); a
