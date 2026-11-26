import streamlit as st
import io
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title='WhiteboardAI', page_icon='W', layout='wide')
st.title('WhiteboardAI - No Error Version')
st.caption('Script + Prompt + Whiteboard + Voice - No HTML')

topic = st.text_input('Topic', value='How People Become Rich')
style = st.selectbox('Style', ['For Kids - Simple', 'For TikTok - Cool', 'For School - Formal'])

c1, c2, c3 = st.columns(3)
with c1:
    gen_script = st.checkbox('Generate SCRIPT?', value=True)
with c2:
    gen_prompt = st.checkbox('Generate PROMPT?', value=False)
with c3:
    gen_video = st.checkbox('Generate WHITEBOARD?', value=True)

d1, d2 = st.columns(2)
with d1:
    voice_lang = st.selectbox('Voice', ['English - US', 'English - UK', 'Filipino'])
with d2:
    speed = st.selectbox('Speed', ['Normal', 'Slow'])

script_input = st.text_area('Script', height=100)
prompt_input = st.text_area('Prompt', height=60)
btn = st.button('GENERATE!', use_container_width=True, type='primary')

def draw_whiteboard(word):
    w = 700
    h = 400
    img = Image.new('RGB', (w, h), color='white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, h], outline='black', width=4)
    d.text((20, 20), 'How People Become Rich', fill='black')
    d.line([(20, 50), (680, 50)], fill='orange', width=4)
    d.text((20, 70), 'Word: ' + word, fill='black')
    hx = 150
    hy = 150
    d.ellipse([hx-20, hy-20, hx+20, hy+20], outline='black', width=3)
    d.line([(hx, hy+20), (hx, hy+90)], fill='black', width=3)
    d.line([(hx, hy+40), (hx-30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+40), (hx+30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+90), (hx-20, hy+130)], fill='black', width=3)
    d.line([(hx, hy+90), (hx+20, hy+130)], fill='black', width=3)
    low = word.lower()
    label = 'KEEP GOING!'
    icon = 'STAR'
    if 'rich' in low or 'money' in low:
        label = 'MONEY GROWS!'
        icon = 'MONEY'
    if 'save' in low:
        label = 'SAVE FIRST!'
        icon = 'PIGGY'
    if 'learn' in low or 'book' in low:
        label = 'LEARN DAILY!'
        icon = 'BOOK'
    if 'work' in low or 'hard' in low:
        label = 'WORK HARD!'
        icon = 'STRONG'
    if 'business' in low:
        label = 'BUSINESS!'
        icon = 'SHOP'
    d.text((450, 150), icon, fill='black')
    d.text((450, 190), label, fill='black')
    d.text((20, 350), 'Tip: Save - Learn - Work - Invest', fill='gray')
    d.text((20, 320), 'Whiteboard is Ready!', fill='green')
    return img

if btn:
    if topic.strip() == '' and (gen_script or gen_prompt or gen_video):
        st.warning('Please type a topic first.')
    else:
        final_script = script_input
        if gen_script:
            final_script = 'Today we will talk about ' + topic + '. Rich people do not become rich by luck. They become rich by habit. First, they save money before they spend money. Second, they learn every day. Third, they work hard and they do not give up. Fourth, they make their money work for them. Fifth, they help other people. So remember, to become rich, you need discipline, learning, hard work, and patience. You just need to start today. Thank you for watching.'
            st.success('SCRIPT:')
            st.code(final_script)
        final_prompt = prompt_input
        if gen_prompt:
            final_prompt = 'Whiteboard video about ' + topic + ', style ' + style + ', hand writing, stickman, clear and fun'
            st.success('PROMPT:')
            st.code(final_prompt)
        if gen_video:
            if not gen_script and script_input.strip() == '':
                st.warning('You chose WHITEBOARD but you have no script.')
            else:
                video_script = final_script if gen_script else script_input
                st.markdown('### YOUR WHITEBOARD')
                words = video_script.split(' ')
                pick = st.selectbox('Pick a word to see drawing', words)
                img = draw_whiteboard(pick)
                st.image(img, use_container_width=True)
                st.success('Whiteboard Generated! Pick a word above to change drawing.')
                st.markdown('### VOICE')
                try:
                    from gtts import gTTS
                    lang = 'en'
                    if 'UK' in voice_lang:
                        lang = 'en'
                    tts = gTTS(text=video_script, lang=lang, slow=False)
                    buf = io.BytesIO()
                    tts.write_to_fp(buf)
                    buf.seek(0)
                    st.audio(buf, format='audio/mp3')
                    st.download_button('DOWNLOAD VOICE MP3', data=buf, file_name='WhiteboardAI-Voice.mp3', mime='audio/mp3')
                except Exception as e:
                    st.info('Voice is not available in cloud. Copy script and use CapCut TTS.')
                    st.code(video_script)
                buf2 = io.BytesIO()
                img.save(buf2, format='PNG')
                buf2.seek(0)
                st.download_button('DOWNLOAD WHITEBOARD IMAGE', data=buf2, file_name='WhiteboardAI.png', mime='image/png')
        if not gen_script and not gen_prompt and not gen_video:
            st.warning('Please check at least one.')
