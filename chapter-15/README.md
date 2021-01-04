<h2>Answers to the Practice Questions from chapter 15</h2>

<p>1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?</p>
<h3><i>Answer</i></h3>

```
import PyPDF2
pdfFileObj = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
```

<p>2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?</p>
<h3><i>Answer</i></h3>
<p>'rb' and 'wb' modes to be opened respectively.</p>

<p>3. How do you acquire a Page object for page 5 from a PdfFileReader object?</p>
<h3><i>Answer</i></h3>

```
pageObj = pdfReader.getPage(4)
```

<p>4. What PdfFileReader variable stores the number of pages in the PDF document?</p>
<h3><i>Answer</i></h3>

```
pdfReader.numPages
```

<p>5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?</p>
<h3><i>Answer</i></h3>

```
pdfReader.decrypt('swordfish')
```

<p>6. What methods do you use to rotate a page?</p>
<h3><i>Answer</i></h3>

```
page = pdfReader.getPage(0)
page.rotateClockwise(90)
```

<p>7. What method returns a Document object for a file named demo.docx?</p>
<h3><i>Answer</i></h3>

```
import docx
doc = docx.Document('demo.docx')
```

<p>8. What is the difference between a Paragraph object and a Run object?</p>
<h3><i>Answer</i></h3>
<p>A paragraphs object is a list of Paragraph objects in the entire document whereas Run is an attribute of paragraphs it returns strings according to different styles of text.</p>

<p>9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?</p>
<h3><i>Answer</i></h3>

```
import docx
doc = docx.Document('demo.docx')
fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)
print(fullText)
```

<p>10. What type of object has bold, underline, italic, strike, and outline variables?</p>
<h3><i>Answer</i></h3>
<p>run object.</p>

<p>11. What is the difference between setting the bold variable to True, False, or None?</p>
<h3><i>Answer</i></h3>
<p>If we set bold variable to True the text will be bolded, If we set bold variable to False the text will be unbolded and If style is set to None, then there will be no style associated with the Paragraph or Run object.</p>

<p>12. How do you create a Document object for a new Word document?</p>
<h3><i>Answer</i></h3>

```
import docx
doc = docx.Document('demo.docx')
```

<p>13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?</p>
<h3><i>Answer</i></h3>

```
import docx
doc = docx.Document('demo.docx')
doc.add_paragraph('Hello there!')
```

<p>14. What integers represent the levels of headings available in Word documents?</p>
<h3><i>Answer</i></h3>
<p>0, 1, 2, 3, 4</p>
