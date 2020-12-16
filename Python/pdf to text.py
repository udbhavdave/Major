import pdf2image

# pdfs = r"U.pdf"
pages = pdf2image.convert_from_path("xyz", 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1

print(i)