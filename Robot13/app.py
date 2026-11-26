import streamlit as st
import random, time

st.set_page_config(page_title="Robot13 V26 - Final", page_icon="🤖", layout="wide")

if "characters" not in st.session_state:
    st.session_state.characters = [
        {"name": "Aria", "hair": "Long Black", "gender": "Female", "clothes": "Hoodie", "emoji": "😊", "style": "Anime", "voice": "Sweet", "face": "Cute", "personality": "Kind and funny"},
        {"name": "Kai", "hair": "Short Spiky", "gender": "Male", "clothes": "Jacket", "emoji": "😎", "style": "Realistic", "voice": "Cool", "face": "Sharp", "personality": "Confident"},
    ]
if "selected_char" not in st.session_state: st.session_state.selected_char = 0
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "history" not in st.session_state: st.session_state.history = []
if "songs" not in st.session_state: st.session_state.songs = []
if "usage" not in st.session_state: st.session_state.usage = 0

st.title("🤖 Robot13 V26 - Final Version")
st.caption("V25 + Song Library + Duet + Karaoke Video + TikTok Caption - No Duplicate Error")

tab_char, tab_chat, tab_suno, tab_video, tab_story, tab_songs, tab_settings = st.tabs(["👥 Characters", "💬 Chat", "🎤 Suno Mode", "🎬 Video", "📖 Story", "🎵 My Songs - V26 BAGO!", "⚙️ Settings"])

# ============ CHARACTERS ============
with tab_char:
    st.subheader("My Characters")
    search = st.text_input("Search character", key="v26_char_search")
    chars = st.session_state.characters
    if search: chars = [c for c in chars if search.lower() in c["name"].lower()]
    cols = st.columns(3)
    for i, c in enumerate(chars):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {c.get('emoji','😊')} {c['name']}")
                st.write(f"Hair: {c.get('hair','')} | Style: {c.get('style','')}")
                st.write(f"Clothes: {c.get('clothes','')} | Voice: {c.get('voice','')}")
                st.write(f"Personality: {c.get('personality','')}")
                if st.button(f"Select {c['name']}", key=f"v26_select_{i}_{c['name']}"):
                    st.session_state.selected_char = st.session_state.characters.index(c); st.rerun()
    st.divider()
    if st.session_state.characters:
        idx = st.session_state.selected_char
        if idx >= len(st.session_state.characters): idx = 0
        cur = st.session_state.characters[idx]
        st.subheader(f"Viewing: {cur['name']}")
        with st.expander("✏️ Edit / Replace Character", expanded=False):
            e_name = st.text_input("Character Name", value=cur["name"], key="v26_edit_name")
            e_hair = st.selectbox("Hair", ["Long Black","Short Spiky","Long White","Blonde","Brown Bob","Pink","Blue","Bald"], key="v26_edit_hair")
            e_gender = st.selectbox("Gender", ["Female","Male","Non-binary","Robot","Other"], key="v26_edit_gender")
            e_clothes = st.selectbox("Clothes", ["Hoodie","Jacket","Dress","Uniform","Streetwear","Armor","Casual"], key="v26_edit_clothes")
            e_emoji = st.selectbox("Emoji", ["😊","😎","🌙","🔥","💜","🤖","✨","😈"], key="v26_edit_emoji")
            e_style = st.selectbox("Style", ["Anime","Realistic","3D","Cartoon","Pixel Art","Cinematic","Pinoy Animation","Whiteboard"], key="v26_edit_style")
            e_voice = st.selectbox("Voice", ["Sweet","Cool","Soft","Deep","Energetic","Calm"], key="v26_edit_voice")
            e_face = st.selectbox("Face", ["Cute","Sharp","Gentle","Bold","Mysterious"], key="v26_edit_face")
            e_personality = st.text_area("Personality", value=cur.get("personality",""), key="v26_edit_personality")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("💾 Save Changes", key="v26_edit_save"):
                    st.session_state.characters[idx] = {"name":e_name,"hair":e_hair,"gender":e_gender,"clothes":e_clothes,"emoji":e_emoji,"style":e_style,"voice":e_voice,"face":e_face,"personality":e_personality}
                    st.success("Saved!"); st.rerun()
            with c2:
                if st.button("🗑️ Delete", key="v26_edit_delete"):
                    st.session_state.characters.pop(idx); st.session_state.selected_char=0; st.rerun()
    with st.expander("➕ Add New Character", expanded=False):
        a_name = st.text_input("Character Name", key="v26_add_name")
        a_hair = st.selectbox("Hair", ["Long Black","Short Spiky","Long White","Blonde","Brown Bob","Pink","Blue","Bald"], key="v26_add_hair")
        a_gender = st.selectbox("Gender", ["Female","Male","Non-binary","Robot","Other"], key="v26_add_gender")
        a_clothes = st.selectbox("Clothes", ["Hoodie","Jacket","Dress","Uniform","Streetwear","Armor","Casual"], key="v26_add_clothes")
        a_emoji = st.selectbox("Emoji", ["😊","😎","🌙","🔥","💜","🤖","✨","😈"], key="v26_add_emoji")
        a_style = st.selectbox("Style", ["Anime","Realistic","3D","Cartoon","Pixel Art","Cinematic","Pinoy Animation","Whiteboard"], key="v26_add_style")
        a_voice = st.selectbox("Voice", ["Sweet","Cool","Soft","Deep","Energetic","Calm"], key="v26_add_voice")
        a_face = st.selectbox("Face", ["Cute","Sharp","Gentle","Bold","Mysterious"], key="v26_add_face")
        a_personality = st.text_area("Personality", key="v26_add_personality")
        if st.button("➕ Create Character", key="v26_add_create"):
            if a_name.strip():
                st.session_state.characters.append({"name":a_name,"hair":a_hair,"gender":a_gender,"clothes":a_clothes,"emoji":a_emoji,"style":a_style,"voice":a_voice,"face":a_face,"personality":a_personality})
                st.success(f"Created {a_name}!"); st.rerun()

# ============ CHAT ============
with tab_chat:
    st.subheader("💬 Chat - Multilingual")
    lang_chat = st.selectbox("Chat Language", ["Taglish","English","Tagalog","Bisaya"], key="v26_chat_lang")
    if st.session_state.characters:
        names = [c["name"] for c in st.session_state.characters]
        chat_idx = st.selectbox("Choose character", names, key="v26_chat_select")
        cur_chat = st.session_state.characters[names.index(chat_idx)]
        st.info(f"Chatting with {cur_chat['emoji']} {cur_chat['name']} - {lang_chat}")
        for m in st.session_state.chat_history:
            with st.chat_message(m["role"]): st.write(m["content"])
        prompt = st.chat_input("Say something...", key="v26_chat_input")
        if prompt:
            st.session_state.chat_history.append({"role":"user","content":prompt})
            st.session_state.chat_history.append({"role":"assistant","content":f"Hi! I'm {cur_chat['name']}. {random.choice(['That is so cool!','Tell me more!','Galing mo boss!'])}"})
            st.rerun()
        if st.button("Clear Chat", key="v26_chat_clear"):
            st.session_state.chat_history=[]; st.rerun()

# ============ SUNO MODE V26 ============
with tab_suno:
    st.subheader("🎤 SUNO MODE - Like Suno AI, But With Your Voice!")
    st.markdown("### ✍️ STEP 1: LYRICS")
    lyrics_mode = st.radio("Lyrics Mode", ["✍️ I Will Write My Own Lyrics","🤖 ROBOT13, Write Lyrics For Me!"], horizontal=True, key="v26_suno_lyrics_mode")
    suno_lyrics = ""
    if "I Will" in lyrics_mode:
        suno_lyrics = st.text_area("Write your lyrics, Boss", "Nay, pahingi po ng baon\n20 pesos lang, gutom na ako\nPero okay lang, kaya ko to", height=120, key="v26_suno_lyrics_input")
    else:
        suno_topic = st.text_input("What is your song about?", "Baon ko 20 pesos lang, pero masaya pa rin ako", key="v26_suno_topic")
        if st.button("🤖 CREATE LYRICS FOR ME!", key="v26_suno_create_lyrics"):
            suno_lyrics = f"[VERSE 1]\n{suno_topic}\nKahit mahirap, masaya pa rin\n[CHORUS]\nKahit 20 pesos lang, kakayanin\nKasi ako si Boss, hindi susuko!"
            st.write(suno_lyrics); st.success("Done!")
        else: suno_lyrics = suno_topic
    st.markdown("### 🎵 STEP 2: MUSIC / TUNE")
    suno_music_mode = st.radio("Music Mode", ["📤 Upload Music / Tune To Copy","🎵 Choose Genre"], horizontal=True, key="v26_suno_music_mode")
    suno_genre = "OPM Pop"
    if "Upload" in suno_music_mode:
        f = st.file_uploader("Upload Music / Tune To Copy (MP3/WAV)", type=["mp3","wav","m4a"], key="v26_suno_music_file")
        if f is not None: st.audio(f); st.success("Music uploaded! Will copy tune, beat, mood.")
    else:
        suno_genre = st.selectbox("Choose Genre", ["🎤 OPM Pop - Like Dilaw","🎤 Bisaya Pop - For CDO","🎤 Rap / Hip-Hop","🎤 Ballad - Like Arthur Nery","🎤 R&B","🎤 Funny / Comedy","🎤 Rock"], key="v26_suno_genre")
        suno_tempo = st.selectbox("Tempo", ["🐢 Slow - 80 BPM","🚶 Normal - 120 BPM","🏃 Fast - 140 BPM"], key="v26_suno_tempo")
    st.markdown("### 🎤 STEP 3: VOICE + 🎤 DUET MODE - V26 BAGO!")
    duet_on = st.checkbox("🎤 DUET MODE ON? - 2 singers!", key="v26_duet_on")
    suno_singer = st.selectbox("Singer 1 - Who Will Sing?", ["🎤 Boss - My Voice Clone","🤖 Nanay - Female, Strong","🤖 Teacher - Female, Angry","🤖 Crush - Female, Sweet","🤖 Kaibigan - Male, Funny"], key="v26_suno_singer1")
    suno_singer2 = "Solo"
    if duet_on:
        suno_singer2 = st.selectbox("Singer 2 - Duet Partner", ["🤖 Crush - Female, Sweet","🤖 Nanay - Female, Strong","🤖 Kaibigan - Male, Funny","🎤 Boss - My Voice Clone"], key="v26_suno_singer2")
        st.info(f"Duet: {suno_singer} + {suno_singer2} - Verse 1 si Singer 1, Chorus sabay!")
    st.markdown("### 🎚️ STEP 4: AUTO-TUNE")
    col1, col2, col3 = st.columns(3)
    with col1:
        auto_tune = st.selectbox("Auto-Tune", ["✅ ON - Not Off-Key","❌ OFF - Raw"], key="v26_suno_autotune")
        tune_key = st.selectbox("Key", ["🎹 C Major","🎹 G Major","🎹 A Minor","🎹 D Major"], key="v26_suno_key")
    with col2:
        tune_pitch = st.slider("Pitch", 0, 100, 50, key="v26_suno_pitch")
        tune_speed = st.slider("Speed", 0, 100, 50, key="v26_suno_speed")
    with col3:
        tune_echo = st.selectbox("Echo", ["🎤 No Echo","🎤 Small Echo","🎤 Big Echo - Concert"], key="v26_suno_echo")
        tune_style = st.selectbox("Singing Style", ["🎤 Normal","🎤 Emotional","🎤 Hype","🎤 Funny"], key="v26_suno_style")
    st.markdown("### 🎙️ CUSTOM AI VOICE")
    custom_voice_name = st.text_input("Custom AI Voice Name", placeholder="Ex: Boses ni Lola", key="v26_custom_voice_name")
    custom_voice_file = st.file_uploader("Upload Custom Voice Sample", type=["mp3","wav","m4a"], key="v26_custom_voice_file")
    if st.button("🎤 CREATE MY SONG NOW!", key="v26_suno_create_song"):
        with st.spinner("Creating your song..."):
            time.sleep(2)
            st.session_state.usage += 1
            new_song = {"title": suno_lyrics[:30] if suno_lyrics else "My Song", "lyrics": suno_lyrics, "singer": suno_singer, "singer2": suno_singer2, "genre": suno_genre, "key": tune_key}
            st.session_state.songs.append(new_song)
            st.session_state.history.append(f"Song: {new_song['title']} - {suno_singer}")
            st.success("✅ DONE! Saved to My Songs! Check My Songs tab!")
            st.write(f"Singer: {suno_singer} | Duet: {suno_singer2} | Genre: {suno_genre} | Auto-Tune: {auto_tune} {tune_key}")

# ============ VIDEO ============
with tab_video:
    st.subheader("🎬 Video Generator - 720p / 1080p + Karaoke")
    if st.session_state.characters:
        names3 = [c["name"] for c in st.session_state.characters]
        vid_idx = st.selectbox("Choose character", names3, key="v26_video_select")
        vc = st.session_state.characters[names3.index(vid_idx)]
        v_scene = st.text_input("Video Scene", key="v26_video_scene", placeholder="Ex: Walking in neon Tokyo")
        v_action = st.text_input("What is character doing?", key="v26_video_action", placeholder="Ex: Dancing")
        v_camera = st.selectbox("Camera", ["Slow Zoom In","Slow Zoom Out","Pan","Orbit","Drone","Close-up"], key="v26_video_camera")
        v_duration = st.selectbox("Duration", ["5s","10s","15s","30s","1 min"], key="v26_video_duration")
        v_mood = st.selectbox("Mood", ["Epic","Happy","Sad","Chill","Action","Romantic","Horror 👻"], key="v26_video_mood")
        v_ratio = st.selectbox("Quality", ["720p - 7MB - Light","1080p - 15MB - HD"], key="v26_video_quality")
        v_size = st.selectbox("Size", ["9:16 - TikTok","16:9 - YouTube","1:1 - Square"], key="v26_video_ratio")
        karaoke_on = st.checkbox("🎤 KARAOKE MODE ON? - Lyrics on screen!", key="v26_karaoke_on")
        if st.button("🎬 Generate Video Prompt", key="v26_video_gen"):
            st.session_state.usage += 1
            st.code(f"VIDEO: {vc['style']} {vc['name']}, {vc['hair']} hair, wearing {vc['clothes']}. Scene: {v_scene}. Action: {v_action}. Camera: {v_camera}. Duration: {v_duration}. Mood: {v_mood}. Quality: {v_ratio} Size: {v_size}. Karaoke: {karaoke_on}", language="text")
            st.success("Copy to Runway / Pika / Sora / Kling / CapCut!")

# ============ STORY ============
with tab_story:
    st.subheader("📖 AI Story + 👻 Horror + ✏️ Whiteboard + 🎬 Anime")
    if st.session_state.characters:
        names4 = [c["name"] for c in st.session_state.characters]
        s_idx = st.selectbox("Choose character", names4, key="v26_story_select")
        sc = st.session_state.characters[names4.index(s_idx)]
        s_genre = st.selectbox("Genre", ["Fantasy","Sci-Fi","Romance","Horror 👻","Action","Comedy 😂","Pinoy Animation 🇵🇭","Whiteboard ✏️","Anime 🎬"], key="v26_story_genre")
        s_place = st.text_input("Where?", key="v26_story_place", placeholder="Ex: Magical school in CDO")
        if st.button("Generate Story", key="v26_story_gen"):
            st.write(f"Once upon a time, {sc['name']} - {sc.get('personality','brave')} with {sc['hair']} hair - found herself in {s_place}. It was a {s_genre} adventure!")
        st.divider()
        st.subheader("🔊 Text-To-Voice")
        tts_text = st.text_input("Type text to speak", key="v26_tts_text")
        tts_voice = st.selectbox("Voice", ["Boss - My Voice Clone","Nanay","Teacher","Crush"], key="v26_tts_voice")
        if st.button("🔊 Speak!", key="v26_tts_speak"):
            st.success(f"Speaking with {tts_voice}: {tts_text}")

# ============ MY SONGS - V26 BAGO ============
with tab_songs:
    st.subheader("🎵 My Songs - Song Library - V26 BAGO!")
    st.write("Lahat ng kanta mo, naka-save dito!")
    if not st.session_state.songs:
        st.info("Wala ka pang kanta. Gawa ka muna sa Suno Mode tab!")
    else:
        for i, s in enumerate(st.session_state.songs):
            with st.container(border=True):
                st.markdown(f"### 🎤 {i+1}. {s.get('title','My Song')}")
                st.write(f"Singer: {s.get('singer','')} | Duet: {s.get('singer2','')} | Genre: {s.get('genre','')} | Key: {s.get('key','')}")
                st.code(s.get('lyrics','')[:500], language="text")
                # TikTok Caption Generator
                if st.button(f"📱 Generate TikTok Caption for Song {i+1}", key=f"v26_tiktok_{i}"):
                    st.code(f"🎤 Bagong kanta ko! {s.get('title','')} 🔥 Boses ko talaga kumakanta! 😱 #fyp #OPM #Robot13 #BisayaPop #Viral #SunoAI #VoiceClone #CDO", language="text")
                    st.success("Copy mo na, post mo na sa TikTok!")
                if st.button(f"🗑️ Delete Song {i+1}", key=f"v26_delete_song_{i}"):
                    st.session_state.songs.pop(i); st.rerun()

# ============ SETTINGS ============
with tab_settings:
    st.subheader("⚙️ Settings + 📊 Limit + 📂 History")
    theme = st.selectbox("Theme", ["Dark","Light","Anime"], key="v26_settings_theme")
    lang = st.selectbox("Language", ["English","Tagalog","Taglish","Bisaya"], key="v26_settings_lang")
    st.write(f"Theme: {theme} | Lang: {lang} | Characters: {len(st.session_state.characters)} | Songs: {len(st.session_state.songs)}")
    st.progress(min(st.session_state.usage / 20, 1.0))
    st.write(f"Used: {st.session_state.usage} / 20 free today")
    st.markdown("### 📂 History")
    for h in reversed(st.session_state.history[-10:]): st.write(f"- {h}")
    if st.button("Reset All", key="v26_settings_reset"):
        st.session_state.characters=[]; st.session_state.chat_history=[]; st.session_state.history=[]; st.session_state.songs=[]; st.session_state.usage=0; st.rerun()
