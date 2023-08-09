import pyttsx3, PyPDF2


#insert name of your pdf file
pdfreader = PyPDF2.pdffilereader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numpages):
    test = pdfreader.getpage(page_num).extracttext()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3/mp4 file 
speaker.save_to_file(clean_text, 'demo.mp3')
speaker.runandwait()

speaker.stop()
