import streamlit as st
import io
from PIL import Image, ImageDraw

st.set_page_config(page_title='WhiteboardAI', page_icon='W', layout='wide')
st.title('WhiteboardAI - Moving + Voice')
st.caption('Animated Whiteboard + Real Voice')

topic = st.text_input('Topic', value='How People Become Rich')
style = st.selectbox('Style', ['For Kids - Simple', 'For TikTok - Cool', 'For School - Formal'])

c1, c2, c3 = st.columns(3)
with c1:
    gen_script = st.checkbox('Generate SCRIPT?', value=True)
with c2:
    gen_prompt = st.checkbox('Generate PROMPT?', value=False)
with c3:
    gen_video = st.checkbox('Generate VIDEO?', value=True)

script_input = st.text_area('Script', height=100)
prompt_input = st.text_area('Prompt', height=60)
btn = st.button('GENERATE!', use_container_width=True, type='primary')

def make_frame(word, idx, all_words):
    w = 700
    h = 400
    img = Image.new('RGB', (w, h), color='white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, h], outline='black', width=4)
    d.text((20, 20), 'How People Become Rich', fill='black')
    d.line([(20, 50), (680, 50)], fill='orange', width=4)
    shown = ' '.join(all_words[:idx+1])
    d.text((20, 70), shown[:60], fill='black')
    d.text((20, 90), shown[60:120], fill='black')
    hx = 100 + (idx % 5) * 50
    hy = 180
    d.ellipse([hx-20, hy-20, hx+20, hy+20], outline='black', width=3)
    d.line([(hx, hy+20), (hx, hy+90)], fill='black', width=3)
    d.line([(hx, hy+40), (hx-30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+40), (hx+30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+90), (hx-20, hy+130)], fill='black', width=3)
    d.line([(hx, hy+90), (hx+20, hy+130)], fill='black', width=3)
    d.text((hx+50, hy+40), '>', fill='red')
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
    if 'help' in low or 'people' in low:
        label = 'HELP OTHERS!'
        icon = 'HEART'
    d.text((450, 170), icon, fill='black')
    d.text((450, 210), label, fill='black')
    d.text((20, 350), 'Tip: Save - Learn - Work - Invest', fill='gray')
    d.text((20, 330), 'Frame ' + str(idx+1) + ' / ' + str(len(all_words)), fill='green')
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
                st.warning('You chose VIDEO but you have no script.')
            else:
                video_script = final_script if gen_script else script_input
                st.markdown('### YOUR MOVING VIDEO')
                words = video_script.split(' ')
                st.info('Wait 3 seconds - generating moving video...')
                frames = []
                for i, wd in enumerate(words):
                    if i % 3 == 0:
                        f = make_frame(wd, i, words)
                        frames.append(f)
                gif_buf = io.BytesIO()
                frames[0].save(gif_buf, format='GIF', save_all=True, append_images=frames[1:], duration=600, loop=0)
                gif_buf.seek(0)
                st.image(gif_buf, use_container_width=True, caption='Your Whiteboard Video - Gumagalaw na!')
                st.download_button('DOWNLOAD VIDEO GIF', data=gif_buf, file_name='WhiteboardAI-Video.gif', mime='image/gif')
                st.markdown('### VOICE - Pindutin PLAY')
                try:
                    from gtts import gTTS
                    tts = gTTS(text=video_script, lang='en', slow=False)
                    buf = io.BytesIO()
                    tts.write_to_fp(buf)
                    buf.seek(0)
                    st.audio(buf, format='audio/mp3')
                    st.download_button('DOWNLOAD VOICE MP3', data=buf, file_name='WhiteboardAI-Voice.mp3', mime='audio/mp3')
                    st.success('Voice Generated! Press PLAY above!')
                except Exception as e:
                    st.error('Voice failed. Check requirements.txt has gTTS. Error: ' + str(e))
        if not gen_script and not gen_prompt and not gen_video:
            st.warning('Please check at least one.')
