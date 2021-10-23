#https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
import fitz
import os
from variable import nom

for k in range(4):
    name=list()
    doc = fitz.open("Source/source%s.pdf"%str(k+1))
    for i in range(len(doc)):
        text = doc[i].get_text("text")
        text=text.split("\n")
        text.pop(0)
        text.pop(len(text)-1)
        text.pop(len(text)-1)
        text.pop(len(text)-1)
        j=0
        while j<len(text):
            if text[j]==nom:
                name.append(text[j]+" "+text[j+1]+" "+text[j+2])
                j=j+3
            else:
                name.append(text[j]+" "+text[j+1])
                j=j+2
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG("Pictures\%s_a\%s.png" % (str(k+1),xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("Pictures\%s_a\%s.png" % (str(k+1),xref))
                pix1 = None
            pix = None
    png_list=os.listdir("Pictures\%s_a"%str(k+1))
    for i in range(len(png_list)):
        png_list[i]=int(png_list[i].split('.')[0])
    png_list=sorted(png_list)
    for i in range(len(name)):
        os.rename("Pictures\%s_a\%s.png"% (str(k+1),str(png_list[i])), "Pictures\%s_a\%s.png" %(str(k+1),name[i]))

