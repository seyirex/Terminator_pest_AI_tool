def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.markdown('<style>body{-webkit-app-region: drag;}</style>', unsafe_allow_html=True)
    st.title("Terminator: An AI Pest Detection App")
    st.text("Build with Streamlit and Tensorflow")
    
    
	
	
    if choice =='About':
        
        intro_markdown = read_markdown_file("./doc/about.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)

    if choice == 'Plant Disease' and enhance_type=='Detection':
        st.header("Plant Disease Detection")
        #c_rate = st.sidebar.slider("Number of classes",1,10)
        image_file = st.file_uploader("Upload Image",type=['jpg'])
        st.markdown("* * *")
        
        if image_file is not None:
            our_image = Image.open(image_file)
            im = our_image.save('./object_detection./images/out.jpg')
            
            if st.button('Process'):
                st.image(in_image , use_column_width=True,channels='RGB')
            st.image(our_image , use_column_width=True,channels='RGB')
            st.balloons()
			
    if choice == 'Plant Disease' and enhance_type == 'Classification':
        st.header("Plant Disease Classification")
        image_input = st.file_uploader("Upload Image",type=['jpg'])
        st.markdown("* * *")
		
        if image_input is not None:
            some_image = Image.open(image_input)
            saved_image = some_image.save('./object_classification./images/out.jpg')   
		
            if st.button('Classify'):
                 st.image(path,use_column_width=True)
                 with st.spinner('Your image is processing'):
                   time.sleep(5)
                 #st.write('**Plant Disease name**: ',cn)
                 st.success(cn)
                 st.balloons()
	
    if enhance_type == 'Treatment' and choice=='Plant Disease':
        data_markdown = read_markdown_file("./treatment/treatment.md")
        st.markdown(data_markdown, unsafe_allow_html=True)
main()

markdown = read_markdown_file("./treatment/.md")
st.markdown(markdown, unsafe_allow_html=True)

image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')