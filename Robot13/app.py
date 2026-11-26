
import streamlit as st
import random

st.set_page_config(page_title="ROBOT13 - AI Video Generator", page_icon="🤖", layout="centered")

st.title("🤖 ROBOT13")
st.subheader("AI Video Generator - For Pinoy Creators")
st.write("Boss, gumawa ka ng viral script in 1 click! Pili ka lang ng topic, at gagawa si ROBOT13 ng script para sayo.")

# --- SIDEBAR ---
st.sidebar.title("⚙️ Settings")
topic = st.sidebar.selectbox("Pili ka ng Topic:", ["Motivation", "Love / Hugot", "Pera / Business", "Funny / Comedy", "Horror", "Basketball", "OFW Life"])
style = st.sidebar.selectbox("Style ng Video:", ["TikTok - Mabilis", "Reels - Pang-FB", "YouTube Shorts", "Pang-Matanda - Mabagal"])
name = st.sidebar.text_input("Pangalan mo (Boss):", "Boss")

# --- MAIN ---
st.markdown("---")
st.header("🎬 1. Gumawa ng Script")

if st.button("🚀 GENERATE SCRIPT - Pindutin Mo!", use_container_width=True):
    hooks = [
        f"Boss, alam mo ba bakit 90% ng tao hindi yumayaman? Kasi {topic} lang sila ng {topic}...",
        f"Huwag mong i-skip to, {name}! Pag nalaman mo to tungkol sa {topic}, magbabago buhay mo!",
        f"3 SECRETS sa {topic} na ayaw sabihin ng mga mayayaman sayo!",
        f"Nagkamali ka, {name}! Akala mo alam mo na ang {topic}, pero mali ka!",
    ]
    bodies = [
        f"Una, sa {topic}, kailangan mo ng disiplina. Pangalawa, kailangan mo ng tiyaga. Pangatlo, kailangan mo maniwala sa sarili mo. Kasi {name}, kung hindi ikaw maniniwala, sino pa?",
        f"Ang totoo niyan, {name}, yung {topic} ay hindi tungkol sa swerte. Tungkol yan sa araw-araw na ginagawa mo. Kahit maliit, basta araw-araw, lalaki yan.",
        f"Isipin mo, {name}. Lahat ng sikat ngayon, nagsimula sa zero. Walang views, walang likes, walang followers. Pero hindi sila sumuko. Ikaw pa kaya?",
    ]
    ctas = [
        "Kung gusto mo pa ng ganito, i-FOLLOW mo ako! Comment ka ng 'GUSTO KO PA'!",
        "I-share mo to sa tropa mo na kailangan makarinig nito! I-like mo na rin!",
        "I-save mo to! Balikan mo pag nawawalan ka na ng pag-asa!",
    ]
    hook = random.choice(hooks)
    body = random.choice(bodies)
    cta = random.choice(ctas)
    
    st.success("✅ Tapos na! Eto yung script mo, Boss!")
    st.subheader("🎤 HOOK (Unang 3 seconds):")
    st.write(hook)
    st.subheader("📖 BODY (Gitna):")
    st.write(body)
    st.subheader("📢 CTA (Dulo - Pang-Follow):")
    st.write(cta)
    st.markdown("---")
    st.info(f"Style: {style} | Topic: {topic}")
    st.write("**Tip ni ROBOT13:** Basahin mo ng malakas, na may gigil! Wag kang mahiya, Boss!")

st.markdown("---")
st.header("🎨 2. Video Ideas")
st.write("Kung wala ka pang idea, eto o:")
if st.button("💡 Bigyan Mo Ako ng Idea"):
    ideas = [
        "POV: Ikaw yung kaibigan na laging nangungutang pero hindi nagbabayad",
        "3 Bagay na ginagawa ng mga tamad pero yumayaman pa rin",
        "Bakit mas masarap ang ulam pag kapitbahay ang nagluto?",
        "OFW: Yung sahod mo sa abroad, pero yung puso mo nasa Pinas",
        "Hugot: Yung nag-reply ka ng 'HAHA' pero gusto mo umiyak",
    ]
    st.warning(random.choice(ideas))

st.markdown("---")
st.header("📝 3. Caption Generator")
caption_topic = st.text_input("Ano yung video mo? Halimbawa: nagluto ako ng adobo")
if st.button("✍️ Gawa Ka ng Caption"):
    if caption_topic:
        st.code(f"POV: {caption_topic} 😂\n\n#robot13 #pinoy #viral #fyp #foryou #tiktokph\n\nFollow mo ako, Boss! Araw-araw may bago!", language="text")
    else:
        st.error("Boss, lagyan mo muna ng topic sa taas!")

st.markdown("---")
st.caption("Made with ❤️ by striker13-tech | ROBOT13 - Para sa mga Pinoy Creator na gustong sumikat!")
