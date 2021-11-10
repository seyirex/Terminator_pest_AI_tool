import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image,ImageOps
from pathlib import Path
import datetime,time

menu_items = {
	'Get help': 'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/',
	'Report a bug': 'https://www.linkedin.com/in/oluwaseyi-gbadamosi-41015216b/',
	'About': '''
	 ## My Custom App

	 Some markdown to show in the About dialog.
	'''
}

st.set_page_config(page_title="Terminator", page_icon="./images/pest-control.png", layout='centered',menu_items=menu_items)
st.set_option('deprecation.showfileUploaderEncoding', False)

# @st.cache(allow_output_mutation=True)
@st.experimental_singleton
def load_model():
	model = tf.keras.models.load_model('./model/keras_model.h5')
	return model


@st.cache
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


def predict_class(image, model):

	# Create the array of the right shape to feed into the keras model
	# The 'length' or number of images you can put into the array is
	# determined by the first position in the shape tuple, in this case 1.
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
	# Replace this with the path to your image
	#resize the image to a 224x224 with the same strategy as in TM2:
	#resizing the image to be at least 224x224 and then cropping from the center
	size = (224, 224)
	image = ImageOps.fit(image, size, Image.ANTIALIAS)

	#turn the image into a numpy array
	image_array = np.asarray(image)
	# Normalize the image
	normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
	# Load the image into the array
	data[0] = normalized_image_array

	# run the inference
	prediction = model.predict(data)
	return np.argmax(prediction, axis=1)

model = load_model()

def main():
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title('Terminator: An AI Pest🐛 Diagnostic tool💯')
    st.text("")
    file = st.file_uploader("Upload an image of a pest 😃 let me blow your mind with what i know", type=["jpg", "png"])
    st.text("")
    st.write("link to images https://drive.google.com/drive/folders/1qz25BA_GICEXRVUSYO3g75UCiw7Zlmcn?usp=sharing")
 
    if file is None:
        st.text('Waiting for upload ⏳')

    else:
        slot = st.empty()
        with st.spinner('Your image is processing ⏳⏳⏳⏳'):
            time.sleep(5)

        test_image = Image.open(file)
        st.image(test_image, caption="Pest Image", width = 400)
        pred = predict_class(test_image, model)
        # st.write(f" Confidence Level {np.max(pred)*100}%")

        if pred == 0:
            markdown = read_markdown_file("./treatment/aphids.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/aphids/banzo.jpg')
            st.image(image, caption='Banzo')
        
        elif pred  == 1:
            markdown = read_markdown_file("./treatment/armyworm.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/armyworm/perfek-315-ec.jpg')
            st.image(image, caption='Perfek-315-ec')
        
        
        elif pred  == 2:
            markdown = read_markdown_file("./treatment/beetle.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/beetle/smash.jpg')
            st.image(image, caption='Smash')
        
        
        elif pred  == 3:
            markdown = read_markdown_file("./treatment/bollworm.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/bollworm/auzar-25-ec.jpg')
            st.image(image, caption='Auzar-25-ec')
        
        
        elif pred  == 4:
            markdown = read_markdown_file("./treatment/grasshopper.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/grasshopper/biostadt-malathion-57-ec.jpg ')
            st.image(image, caption='Biostadt-malathion-57-ec')
        
        
        elif pred  == 5:
            markdown = read_markdown_file("./treatment/mites.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/mites/bioclaim.jpg')
            st.image(image, caption='Bioclaim')
        
        
        elif pred  == 6:
            markdown = read_markdown_file("./treatment/sawfly.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/sawfly/krush.jpg')
            st.image(image, caption='krush')
        
        
        elif pred  == 7:
            markdown = read_markdown_file("./treatment/stem_borer.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/stem_borer/cartop.jpg')
            st.image(image, caption='Cartop')
        
        
        elif pred  == 8:
            markdown = read_markdown_file("./treatment/.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('Eagle-Thripan-Bio-Miticide.jpg')
            st.image(image, caption='Eagle-Thripan-Bio-Miticide')
        
        
        elif pred  == 9:
            markdown = read_markdown_file("./treatment/.md")
            st.markdown(markdown, unsafe_allow_html=True)
            image = Image.open('./images/whitefly/reno.jpg')
            st.image(image, caption='Reno')
        
        
        else:
            st.write("Unkown pests please try another pest image.")

if __name__=='__main__':
    main()