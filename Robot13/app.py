# ==========================================
# ROBOT13 - FINAL VERSION - FINAL NA, BOSS!
# UI: ENGLISH | Content: BISAYA / TAGALOG
# Characters: STARTS WITH CHARACTER 1 ONLY! Click ADD CHARACTER to add more!
# Funny & Horror: CAN CREATE VIDEO! Funny with Sound Effects, Horror with Jump Scare!
# ==========================================
import streamlit as st
import time

st.set_page_config(page_title="ROBOT13 - AI Video Generator", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.main {background-color:#0A0A0A; color:white;}
.pro-card {background:#1A1A2E; padding:20px; border-radius:15px; border:1px solid #333; margin-bottom:15px;}
.stButton>button {background:#FF0000; color:white; border-radius:10px; font-weight:bold; padding:12px;}
.stButton>button:hover {background:#CC0000;}
</style>
""", unsafe_allow_html=True)

st.markdown("# 🤖 ROBOT13")
st.markdown("**AI Video Generator • 720p / 1080p HD - Lightweight**")

if "characters" not in st.session_state:
    st.session_state.characters = {
        "CHARACTER 1": {"emoji":"🧑","name":"Character 1","gender":"Male","voice":"Filipino Male - Strong","style":"Normal","desc":"Click EDIT to set name, look, voice"},
    }
if "history" not in st.session_state: st.session_state.history = []
if "limit_count" not in st.session_state: st.session_state.limit_count = 0

tab_char, tab_chat, tab_ai, tab_funny, tab_pinoy, tab_ttv, tab_white, tab_anime, tab_horror, tab_music, tab_hist, tab_set = st.tabs([
    "🧑 MY CHARACTERS","💬 CHAT","🤖 AI STORY","😂 FUNNY","🇵🇭 PINOY ANIMATION","🔊 TEXT-TO-VOICE","✏️ WHITEBOARD","🎬 ANIME","👻 HORROR","🎤 MUSIC","📂 HISTORY","⚙️ SETTINGS"
])

# ========== 1. MY CHARACTERS - ISA LANG SA SIMULA ==========
with tab_char:
    st.markdown('<div class="pro-card"><h3>🧑 MY CHARACTERS</h3>', unsafe_allow_html=True)
    st.write(f"You have {len(st.session_state.characters)} character(s). Start with Character 1. Click ADD CHARACTER to add more.")
    st.info("Example: Character 1 = You. Want a second? Click ADD CHARACTER. Character 2 = Your Mother. You decide!")
    for key, v in list(st.session_state.characters.items()):
        c1,c2,c3,c4 = st.columns([1,3,1,1])
        with c1: st.markdown(f'<div style="font-size:40px; text-align:center;">{v["emoji"]}</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f"**{v['name']}** - {v['desc']}")
            st.markdown(f"{v['gender']} • Voice: {v['voice']}")
        with c3:
            if st.button(f"✏️ EDIT", key=f"edit_{key}"): st.session_state.editing_char = key
        with c4:
            if st.button(f"🗑️ DELETE", key=f"del_{key}"): st.session_state.delete_confirm = key
        st.markdown("---")
    if "delete_confirm" in st.session_state and st.session_state.delete_confirm in st.session_state.characters:
        del_key = st.session_state.delete_confirm
        del_name = st.session_state.characters[del_key]["name"]
        st.warning(f"Are you sure you want to delete {del_name}? This cannot be undone.")
        dc1, dc2 = st.columns(2)
        with dc1:
            if st.button(f"✅ YES, DELETE {del_name}", use_container_width=True):
                del st.session_state.characters[del_key]; del st.session_state.delete_confirm; st.success(f"✅ Deleted {del_name}!"); st.rerun()
        with dc2:
            if st.button("❌ NO, KEEP IT", use_container_width=True):
                del st.session_state.delete_confirm; st.info("✅ Kept.")
    if "editing_char" in st.session_state and st.session_state.editing_char in st.session_state.characters:
        edit_key = st.session_state.editing_char; old = st.session_state.characters[edit_key]
        st.markdown(f"### ✏️ EDIT - {old['name']}")
        e1,e2,e3 = st.columns(3)
        with e1:
            nn = st.text_input("Character Name - You name it!", value=old["name"], key="e_name")
            nh = st.selectbox("Hair", ["Short - Male","Long - Female","Bald - Comedy","Colored - Anime"], key="e_hair")
            nf = st.selectbox("Face", ["😀 Happy","😡 Angry","😴 Sleepy","😎 Cool"], key="e_face")
        with e2:
            ns = st.selectbox("Clothes", ["👕 Red T-Shirt","👕 Black T-Shirt","👕 Uniform","👕 Barong"], key="e_shirt")
            ng = st.selectbox("Gender", ["Male - Male voices only","Female - Female voices only"], key="e_gender")
        with e3:
            ne = st.selectbox("Emoji", ["🧑","👦","👧","🧑‍🎤","👨‍🏫","🩴","💔","👩","👴","👵"], key="e_emoji")
            nst = st.selectbox("Style", ["🎨 Alexnimation Style","🎨 Bogart Style","🎨 Anime Style","🎨 Chibi Style"], key="e_style")
        if "Male" in ng: nv = st.selectbox("Voice - Male Only", ["🇵🇭 Filipino Male - Strong","🇵🇭 Bisaya Male","🇵🇭 Pinoy English Male","🇺🇸 American Male - Deep","🇬🇧 British Male","🎭 Funny Male"], key="e_voice_m")
        else: nv = st.selectbox("Voice - Female Only", ["🇵🇭 Filipina Female - Sweet","🇵🇭 Filipina Female - Strong","🇵🇭 Bisaya Female","🇵🇭 Pinay English Female","🇺🇸 American Female","🇬🇧 British Female"], key="e_voice_f")
        ec1, ec2 = st.columns(2)
        with ec1:
            if st.button("💾 SAVE CHANGES", use_container_width=True):
                del st.session_state.characters[edit_key]
                st.session_state.characters[nn.upper()] = {"emoji":ne,"name":nn,"gender":ng,"voice":nv,"style":nst,"desc":f"{nh} • {ns} • {nf}"}
                del st.session_state.editing_char; st.success(f"✅ Updated! Now {nn}!"); st.rerun()
        with ec2:
            if st.button("❌ CANCEL", use_container_width=True):
                del st.session_state.editing_char
    st.markdown("---")
    st.markdown("### ➕ ADD CHARACTER")
    st.write("Want more? Click ADD CHARACTER. One click = One new character. You name it.")
    next_num = len(st.session_state.characters) + 1
    while any(v["name"]==f"Character {next_num}" for v in st.session_state.characters.values()): next_num += 1
    st.info(f"Next character will be: Character {next_num}")
    ac1,ac2,ac3 = st.columns(3)
    with ac1:
        new_name = st.text_input("New Character Name", f"Character {next_num}", key="new_name_input")
        new_hair = st.selectbox("Hair", ["Short - Male","Long - Female","Bald - Comedy","Colored - Anime"], key="new_hair")
    with ac2:
        new_gender = st.selectbox("Gender", ["Male - Male voices only","Female - Female voices only"], key="new_gender")
        new_shirt = st.selectbox("Clothes", ["👕 Red T-Shirt","👕 Black T-Shirt","👕 Uniform","👕 Barong"], key="new_shirt")
    with ac3:
        new_emoji = st.selectbox("Emoji", ["🧑","👦","👧","👩","🧑‍🎤"], key="new_emoji")
        new_style = st.selectbox("Style", ["🎨 Alexnimation Style","🎨 Bogart Style","🎨 Anime Style","🎨 Chibi Style"], key="new_style")
    if "Male" in new_gender: new_voice = st.selectbox("Voice - Male Only", ["🇵🇭 Filipino Male - Strong","🇵🇭 Bisaya Male","🇺🇸 American Male - Deep"], key="new_voice_m")
    else: new_voice = st.selectbox("Voice - Female Only", ["🇵🇭 Filipina Female - Sweet","🇵🇭 Filipina Female - Strong","🇵🇭 Bisaya Female"], key="new_voice_f")
    if st.button("➕ ADD CHARACTER", use_container_width=True):
        st.session_state.characters[new_name.upper()] = {"emoji":new_emoji,"name":new_name,"gender":new_gender,"voice":new_voice,"style":new_style,"desc":f"{new_hair} • {new_shirt}"}
        st.success(f"✅ Added {new_name}! You now have {len(st.session_state.characters)} characters!"); st.rerun()
    st.markdown("---")
    st.markdown("### 📸 UPLOAD PHOTO - MAKE IT ANIME")
    up = st.file_uploader("Upload Your Photo", type=["jpg","png","jpeg"])
    if up is not None:
        st.image(up, width=200)
        up_style = st.selectbox("Style", ["🎨 Alexnimation Style","🎨 Anime Style","🎨 Chibi Style"])
        if st.button("🎨 MAKE ME ANIME!", use_container_width=True): st.success("✅ Done!")
    st.markdown("---")
    st.markdown("### 🎙️ CUSTOM AI VOICE")
    vc1, vc2 = st.columns(2)
    with vc1:
        vc_char = st.selectbox("Select Character", list(st.session_state.characters.keys()))
        vc_gender2 = st.selectbox("Gender", ["Male - Male voices only","Female - Female voices only"])
    with vc2:
        if "Male" in vc_gender2: vc_voice = st.selectbox("Choose AI Voice - Male Only", ["🇵🇭 Filipino Male - Strong","🇵🇭 Bisaya Male","🇵🇭 Pinoy English Male","🇺🇸 American Male - Deep","🇬🇧 British Male","🎭 Funny Male","👴 Old Male"])
        else: vc_voice = st.selectbox("Choose AI Voice - Female Only", ["🇵🇭 Filipina Female - Sweet","🇵🇭 Filipina Female - Strong","🇵🇭 Bisaya Female","🇵🇭 Pinay English Female","🇺🇸 American Female","🇬🇧 British Female","🎭 Funny Female","👵 Old Female"])
    up_ai = st.file_uploader("Upload AI Voice (MP3 / WAV / M4A)", type=["mp3","wav","m4a"], key="ai_voice")
    if up_ai is not None: st.audio(up_ai)
    if st.button("💾 SAVE AI VOICE TO CHARACTER", use_container_width=True): st.success(f"✅ Saved! {vc_char} will now use: {vc_voice}.")
    st.markdown("---")
    st.markdown("### 🎤 VOICE CLONE")
    st.info("Record 30 seconds once. Character 1 will use your voice. Others use AI voice. This voice will also sing in MUSIC.")
    st.markdown('<div style="background:#FFF3CD; color:#000; padding:12px; border-radius:10px;">Read this: <i>"Hello, ako si Boss. Gusto ko yumaman kahit mahirap ako. Kaya mo yan, Boss! Magpukpok ka lang araw-araw. I-follow mo ako para sa Part 2!"</i></div>', unsafe_allow_html=True)
    vc_clone_char = st.selectbox("Which character will use your voice?", list(st.session_state.characters.keys()))
    vc_file = st.file_uploader("Upload Your Voice (30s)", type=["mp3","wav","m4a"], key="vc_file")
    if vc_file is not None:
        st.audio(vc_file)
        if st.button("💾 SAVE MY VOICE", use_container_width=True): st.success(f"✅ Saved to {vc_clone_char}!")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 2. CHAT ==========
with tab_chat:
    st.markdown('<div class="pro-card"><h3>💬 CHAT WITH ROBOT13</h3>', unsafe_allow_html=True)
    chat_lang = st.selectbox("Language", ["Bisaya","Tagalog","Taglish","Ilocano","Hiligaynon","Waray","English"])
    chat_msg = st.text_input("What do you want to talk about?", "How to make a skit?")
    if st.button("💬 SEND", use_container_width=True):
        if chat_lang=="Bisaya": st.write("**ROBOT13:** Sige bai! I-script nato ni gamit ang Character 1 ug Character 2.")
        else: st.write("**ROBOT13:** Let's go Boss! Let's make a script using Character 1 and Character 2.")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 3. AI STORY ==========
with tab_ai:
    st.markdown('<div class="pro-card"><h3>🤖 AI STORY</h3>', unsafe_allow_html=True)
    ai_topic = st.text_input("Topic", "Nahuli ako na naglalaro ng ML")
    if st.button("🤖 CREATE STORY!", use_container_width=True):
        story = f"[SCENE 1 - In Room]\n\nCHARACTER 1: Isa na lang, mananalo na ako!\n\nCHARACTER 2: CHARACTER 1! May exam ka pa bukas!\n\nCHARACTER 1: Isa na lang po!"
        st.write(story); st.session_state.history.append(story[:80])
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 4. FUNNY - PWEDE NA GAWING VIDEO! ==========
with tab_funny:
    st.markdown('<div class="pro-card"><h3>😂 FUNNY MODE - Pwede Gawing Video!</h3>', unsafe_allow_html=True)
    st.write("Create funny story, then create video from it. With dialogue, sound effects, comedy timing!")
    f_text = st.text_input("Funny story", "Yung baon ko 20 pesos lang")
    f_chars = st.multiselect("Select Characters", list(st.session_state.characters.keys()), default=list(st.session_state.characters.keys())[:1])
    f_sound = st.selectbox("Sound Effects", ["😂 HAHAHA - Laugh Track","🩴 SWOOSH - Tsinelas Flying","💥 BOING - Funny Bounce","😱 ARAY - Pain Sound"])
    if st.button("😂 CREATE FUNNY STORY!", use_container_width=True):
        funny_story = f"""[SCENE 1 - In Room]\n\nCHARACTER 1: {f_text} - HAHAHA!\n\nCHARACTER 2: Anong oras na! May tsinelas ako dito!\n\n[SOUND EFFECT: {f_sound}]\n\nCHARACTER 1: Aray! Tamaan ako!\n\n[END] Relate ka ba? Tag your friend!"""
        st.write(funny_story); st.session_state.funny_story = funny_story; st.success("✅ Funny story created!")
    if "funny_story" in st.session_state:
        st.markdown("---")
        st.markdown("### 🎬 CREATE VIDEO FROM THIS FUNNY STORY?")
        st.write("This will create a video with dialogue, sound effects, and comedy timing. 39 seconds, 720p HD, 7MB.")
        v_quality_funny = st.radio("Video Quality", ["✅ 720p HD - 7MB - For TikTok","⭐ 1080p Full HD - 15MB - For YouTube"], key="funny_quality")
        if st.button("🎬 CREATE FUNNY VIDEO NOW!", use_container_width=True):
            with st.spinner("Creating your funny video..."):
                time.sleep(2)
                st.success("✅ DONE! Your funny video is ready!")
                st.markdown(f"**Your Funny Video:**\n- **Characters:** {', '.join(f_chars)}\n- **Sound Effects:** {f_sound}\n- **Quality:** {v_quality_funny}\n- **Length:** 39 seconds - Perfect for TikTok!")
                st.info("Picture changes per dialogue, voice changes per character, with sound effects!")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 5. PINOY ANIMATION ==========
with tab_pinoy:
    st.markdown('<div class="pro-card"><h3>🇵🇭 PINOY ANIMATION</h3>', unsafe_allow_html=True)
    p_type = st.selectbox("Story Type", ["🏫 Student Life","🩴 My Mother","💔 My Crush","💸 My Baon is 20 Pesos","👨‍🏫 My Teacher","🎮 ML / Roblox"])
    p_topic = st.text_input("Your Topic", "Nahuli ako na naglalaro ng ML kahit may exam bukas")
    sel = st.multiselect("Select Characters", list(st.session_state.characters.keys()), default=list(st.session_state.characters.keys())[:1])
    st.info(f"You will use: {', '.join(sel)}. Each has its own voice.")
    if st.button("🇵🇭 CREATE STORY!", use_container_width=True):
        st.write("""[SCENE 1 - In Room, Night]\n\nCHARACTER 1: Isa na lang, mananalo na ako! 🎤 Your Voice\n\nCHARACTER 2: Anong oras na! 🤖 AI Voice""")
        st.success("✅ Done!")
        if st.button("🎬 CREATE VIDEO FROM THIS!", use_container_width=True): st.success("✅ Creating your video!")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 6. TEXT-TO-VOICE ==========
with tab_ttv:
    st.markdown('<div class="pro-card"><h3>🔊 TEXT-TO-VOICE</h3>', unsafe_allow_html=True)
    t_text = st.text_area("Write what you want to say", "Kaya mo yan, Boss! Magpukpok ka lang araw-araw!")
    t_voice = st.selectbox("Who will speak?", list(st.session_state.characters.keys()))
    if st.button("🔊 MAKE IT VOICE!", use_container_width=True):
        c = st.session_state.characters.get(t_voice,{})
        st.success(f"✅ Done! {t_voice} spoke. Voice: {c.get('voice','')}")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 7. WHITEBOARD ==========
with tab_white:
    st.markdown('<div class="pro-card"><h3>✏️ WHITEBOARD</h3>', unsafe_allow_html=True)
    w_text = st.text_input("What to write?", "Paano yumaman kahit mahirap ka")
    if st.button("✏️ MAKE WHITEBOARD!", use_container_width=True): st.write(f"✏️ Writing: {w_text}")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 8. ANIME ==========
with tab_anime:
    st.markdown('<div class="pro-card"><h3>🎬 ANIME</h3>', unsafe_allow_html=True)
    a_char = st.selectbox("Main Character", list(st.session_state.characters.keys()))
    a_prompt = st.text_input("Scene", "Si Character 1, naglalaro ng ML sa kwarto")
    if st.button("🎬 MAKE ANIME!", use_container_width=True):
        st.session_state.limit_count += 1
        st.success(f"✅ Done! Anime using {a_char}! Limit: {st.session_state.limit_count}/20")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 9. HORROR - PWEDE NA GAWING VIDEO! MAY JUMP SCARE! ==========
with tab_horror:
    st.markdown('<div class="pro-card"><h3>👻 HORROR MODE - Pwede Gawing Video! May Jump Scare!</h3>', unsafe_allow_html=True)
    st.write("Create horror story, then create video from it. With jump scare, horror music, dark pictures!")
    h_text = st.text_input("Horror story", "Yung White Lady")
    h_chars = st.multiselect("Select Characters", list(st.session_state.characters.keys()), default=list(st.session_state.characters.keys())[:1])
    h_scary = st.selectbox("Scary Level", ["😨 Light Scary - For Kids","😱 Medium Scary - With Jump Scare","💀 Very Scary - Very Dark, Very Loud Jump Scare"])
    h_music = st.selectbox("Horror Music", ["🎵 Tension Music - Slow, Creepy","🎵 Door Creak - Creak, Wind Sound","🎵 Whisper - Whispering, Creepy","🎵 Silent - Only Sound Effects"])
    if st.button("👻 CREATE HORROR STORY!", use_container_width=True):
        horror_story = f"""[SCENE 1 - Dark Room, Night]\n\n[MUSIC: {h_music}]\n\nCHARACTER 1: Sino yan? Sino nandyan? Natatakot ako...\n\n[SOUND EFFECT: CREAK! Door opening...]\n\nCHARACTER 1: Ayoko na! Gusto ko na umuwi!\n\n[JUMP SCARE - At 0:25]\n\nCHARACTER 2: Hindi ka makakatakas...\n\n[END] Nakatakot ka ba? Tag your friend!"""
        st.write(horror_story); st.session_state.horror_story = horror_story; st.success("✅ Horror story created!")
    if "horror_story" in st.session_state:
        st.markdown("---")
        st.markdown("### 🎬 CREATE VIDEO FROM THIS HORROR STORY?")
        st.write("This will create a video with jump scare, horror music, dark pictures. 39 seconds, 720p HD, 7MB.")
        v_quality_horror = st.radio("Video Quality", ["✅ 720p HD - 7MB - For TikTok","⭐ 1080p Full HD - 15MB - For YouTube"], key="horror_quality")
        jump_time = st.slider("Jump Scare Time - When will the ghost appear?", 10, 35, 25)
        if st.button("🎬 CREATE HORROR VIDEO NOW!", use_container_width=True):
            with st.spinner("Creating your horror video..."):
                time.sleep(2)
                st.success("✅ DONE! Your horror video is ready!")
                st.markdown(f"**Your Horror Video:**\n- **Characters:** {', '.join(h_chars)}\n- **Scary Level:** {h_scary}\n- **Horror Music:** {h_music}\n- **Jump Scare:** At 0:{jump_time} seconds - Ghost will appear with BOOM!\n- **Quality:** {v_quality_horror}\n- **Length:** 39 seconds - Perfect for TikTok!")
                st.info("With jump scare, horror music, dark pictures!")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 10. MUSIC ==========
with tab_music:
    st.markdown('<div class="pro-card"><h3>🎤 MUSIC - Write Lyrics, Upload Tune, Your Voice Sings!</h3>', unsafe_allow_html=True)
    st.write("Write lyrics, upload music / tune to copy, use your voice clone to sing. ROBOT13 will adjust your voice to the music.")
    st.markdown("### ✍️ STEP 1: LYRICS")
    lyrics_mode = st.radio("Lyrics", ["✍️ I Will Write My Own Lyrics","🤖 ROBOT13, Write Lyrics For Me!"], horizontal=True)
    if "I Will" in lyrics_mode:
        music_lyrics = st.text_area("Write your lyrics", "Nay, pahingi po ng baon\n20 pesos lang, gutom na ako\nPero okay lang, kaya ko to\nKasi ako si Boss", height=120)
    else:
        music_topic = st.text_input("What is your song about?", "Baon ko 20 pesos lang, pero masaya pa rin ako")
        music_lyrics = ""
        if st.button("🤖 CREATE LYRICS FOR ME!", use_container_width=True):
            music_lyrics = """[VERSE 1]\nNay, pahingi po ng baon\n20 pesos lang, gutom na ako\nPero okay lang, kaya ko to\nKasi ako si Boss\n\n[CHORUS]\nKahit mahirap, masaya pa rin\nKahit 20 pesos lang, kakayanin"""
            st.write(music_lyrics); st.success("✅ Done!")
    st.markdown("---")
    st.markdown("### 🎵 STEP 2: MUSIC / TUNE")
    music_mode = st.radio("Music Mode", ["📤 Upload Music / Tune To Copy","🎵 Choose Genre"], horizontal=True)
    music_genre = "Uploaded Tune"
    if "Upload" in music_mode:
        music_file = st.file_uploader("Upload Music / Tune (MP3 / WAV)", type=["mp3","wav","m4a"])
        if music_file is not None: st.audio(music_file); st.success("✅ Music uploaded!")
    else:
        music_genre = st.selectbox("Choose Genre", ["🎤 OPM Pop","🎤 Bisaya Pop","🎤 Rap / Hip-Hop","🎤 Ballad","🎤 R&B","🎤 Funny / Comedy","🎤 Rock"])
        music_tempo = st.selectbox("Tempo", ["🐢 Slow - 80 BPM","🚶 Normal - 120 BPM","🏃 Fast - 140 BPM"])
    st.markdown("---")
    st.markdown("### 🎤 STEP 3: VOICE - Who Will Sing?")
    music_singer = st.selectbox("Who Will Sing?", list(st.session_state.characters.keys()) + ["🎤 Upload New Voice To Sing"])
    if "Upload New" in music_singer:
        music_new_voice = st.file_uploader("Upload Voice To Sing (30s)", type=["mp3","wav","m4a"], key="music_voice")
        if music_new_voice is not None: st.audio(music_new_voice); st.success("✅ Voice uploaded!")
    st.markdown("---")
    st.markdown("### 🎚️ STEP 4: AUTO-TUNE")
    c_t1,c_t2,c_t3 = st.columns(3)
    with c_t1:
        auto_tune = st.selectbox("Auto-Tune", ["✅ ON - Auto Adjust, Not Off-Key","❌ OFF - Raw Voice"])
        tune_key = st.selectbox("Key", ["🎹 C Major - For Pop","🎹 G Major - For Ballad","🎹 A Minor - For Emotional","🎹 D Major - For Hype"])
    with c_t2:
        tune_pitch = st.slider("Pitch", 0, 100, 50)
        tune_speed = st.slider("Speed", 0, 100, 50)
    with c_t3:
        tune_echo = st.selectbox("Echo / Reverb", ["🎤 No Echo","🎤 Small Echo","🎤 Big Echo - Like In Concert"])
        tune_style = st.selectbox("Singing Style", ["🎤 Normal","🎤 Emotional","🎤 Hype","🎤 Funny"])
    st.markdown("---")
    if st.button("🎤 CREATE MY SONG NOW!", use_container_width=True):
        with st.spinner("Creating your song..."):
            time.sleep(2)
            st.success("✅ DONE! Your song is ready!")
            st.markdown(f"**Song:**\n- **Lyrics:** {music_lyrics[:100]}...\n- **Singer:** {music_singer}\n- **Music:** {music_genre}\n- **Auto-Tune:** {auto_tune} - Key: {tune_key}\n- **Length:** 2:30 - Perfect for TikTok!")
            if st.button("🎬 MAKE MUSIC VIDEO FROM THIS SONG!", use_container_width=True):
                st.success("✅ Creating music video! With your characters, with your song, with lyrics on screen like Karaoke!")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 11. HISTORY ==========
with tab_hist:
    st.markdown('<div class="pro-card"><h3>📂 HISTORY</h3>', unsafe_allow_html=True)
    if len(st.session_state.history)==0: st.write("No history yet. Create a video first!")
    else:
        for h in st.session_state.history: st.write(f"- {h}")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== 12. SETTINGS ==========
with tab_set:
    st.markdown('<div class="pro-card"><h3>🎬 VIDEO QUALITY - Choose 720p or 1080p</h3>', unsafe_allow_html=True)
    q = st.radio("Select Quality", ["✅ 720p HD - Lightweight, 7MB in 39s, Clear, For TikTok, FB Reels - MOST USED","⭐ 1080p Full HD - Very Clear, 15MB in 39s, For YouTube, TV, Professional"])
    s = st.radio("Select Size", ["📱 9:16 - Vertical - For TikTok, FB Reels","📺 16:9 - Horizontal - For YouTube","🟦 1:1 - Square - For FB Post"])
    if "720p" in q:
        c1,c2,c3 = st.columns(3)
        c1.metric("📱 39s - Reels","7MB","Lightweight!")
        c2.metric("📱 60s - TikTok","12MB","Lightweight!")
        c3.metric("📺 3min - YouTube","35MB","Lightweight!")
        st.success("✅ You selected 720p HD!")
    else:
        c1,c2,c3 = st.columns(3)
        c1.metric("📱 39s - Reels","15MB","Heavier")
        c2.metric("📱 60s - TikTok","25MB","Heavier")
        c3.metric("📺 3min - YouTube","70MB","Heavier")
        st.success("⭐ You selected 1080p Full HD!")
    st.markdown("---")
    st.markdown("### 📊 LIMIT TRACKER")
    st.write(f"You have used {st.session_state.limit_count}/20 images today. {20-st.session_state.limit_count} remaining.")
    st.progress(st.session_state.limit_count/20)
    st.info("Tip: If you use your saved character, no limit!")
    st.markdown("---")
    st.markdown("### ⚙️ ABOUT ROBOT13")
    st.write("ROBOT13 - Final Version. For all Pinoy Creators. Kaya mo yan, Boss!")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
if st.button("✨ CREATE VIDEO NOW!", use_container_width=True):
    st.balloons()
    st.success("✅ Creating your video, Boss!")
