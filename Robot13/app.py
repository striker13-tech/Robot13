import streamlit as st
import io
from PIL import Image, ImageDraw

st.set_page_config(page_title='WhiteboardAI', page_icon='W', layout='wide')
st.title('WhiteboardAI - Topic Drawing + Voice')
st.caption('Real Drawings Per Topic + Real Voice')

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

def draw_scene(idx, title, scene_text):
    w = 700
    h = 480
    img = Image.new('RGB', (w, h), color='white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, h], outline='black', width=4)
    d.text((20, 15), title.upper(), fill='black')
    d.line([(20, 45), (680, 45)], fill='orange', width=4)
    d.text((20, 60), scene_text[:70], fill='black')
    d.text((20, 80), scene_text[70:140], fill='black')
    hx = 150
    hy = 220
    d.ellipse([hx-20, hy-20, hx+20, hy+20], outline='black', width=3)
    d.line([(hx, hy+20), (hx, hy+90)], fill='black', width=3)
    d.line([(hx, hy+40), (hx-30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+40), (hx+30, hy+60)], fill='black', width=3)
    d.line([(hx, hy+90), (hx-20, hy+130)], fill='black', width=3)
    d.line([(hx, hy+90), (hx+20, hy+130)], fill='black', width=3)
    d.text((hx+50, hy+30), '>', fill='red')
    # DRAWING PER SCENE - TOPIC DRAWING
    if idx == 0:
        # PIGGY BANK
        d.ellipse([450, 200, 620, 300], outline='black', width=3)
        d.ellipse([460, 210, 490, 240], outline='black', width=2)
        d.text((500, 240), 'PIGGY BANK', fill='black')
        d.text((450, 320), 'SAVE MONEY FIRST!', fill='black')
        d.text((450, 150), '$ $ $', fill='green')
    elif idx == 1:
        # BOOK
        d.rectangle([450, 180, 620, 300], outline='black', width=3)
        d.line([(535, 180), (535, 300)], fill='black', width=2)
        d.text((470, 230), 'BOOK', fill='black')
        d.text((550, 230), 'LEARN', fill='black')
        d.text((450, 320), 'LEARN EVERY DAY!', fill='black')
    elif idx == 2:
        # HOUSE + SUN
        d.ellipse([580, 140, 640, 200], outline='orange', width=3)
        d.rectangle([450, 220, 600, 320], outline='black', width=3)
        d.polygon([(440, 220), (525, 160), (610, 220)], outline='black', width=3)
        d.text((450, 340), 'WORK HARD - HOUSE!', fill='black')
    elif idx == 3:
        # MONEY BAG
        d.ellipse([470, 200, 600, 320], outline='green', width=4)
        d.text((510, 240), '$', fill='green')
        d.text((450, 340), 'MONEY GROWS!', fill='black')
        d.text((450, 150), 'RICH!', fill='green')
    else:
        # HEART - HELP OTHERS
        d.ellipse([470, 200, 530, 260], outline='red', width=3)
        d.ellipse([540, 200, 600, 260], outline='red', width=3)
        d.polygon([(460, 240), (535, 330), (610, 240)], outline='red', width=3)
        d.text((450, 350), 'HELP OTHERS!', fill='black')
    d.text((20, 430), 'Tip: Save - Learn - Work - Invest - Help', fill='gray')
    d.text((20, 410), 'Scene ' + str(idx+1) + ' / 5', fill='green')
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
                st.markdown('### YOUR MOVING VIDEO - TOPIC DRAWINGS')
                scenes = []
                scenes.append('First, they save money before they spend money.')
                scenes.append('Second, they learn every day.')
                scenes.append('Third, they work hard and they do not give up.')
                scenes.append('Fourth, they make their money work for them.')
                scenes.append('Fifth, they help other people.')
                frames = []
                for i, s in enumerate(scenes):
                    for k in range(4):
                        f = draw_scene(i, topic, s)
                        frames.append(f)
                gif_buf = io.BytesIO()
                frames[0].save(gif_buf, format='GIF', save_all=True, append_images=frames[1:], duration=700, loop=0)
                gif_buf.seek(0)
                st.image(gif_buf, use_container_width=True, caption='Topic Video - Piggy, Book, House, Money, Heart!')
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
                    st.success('Voice OK! Press PLAY!')
                except Exception as e:
                    st.error('Voice failed. Wala pa requirements.txt! Gawa ka ng requirements.txt tapos REBOOT! Error: ' + str(e))
        if not gen_script and not gen_prompt and not gen_video:
            st.warning('Please check at least one.')
