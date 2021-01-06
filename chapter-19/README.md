<h2>Answers to the Practice Questions from chapter 19</h2>

<p>1. What is an RGBA value?</p>
<h3><i>Answer</i></h3>
<p>Images are made of pixels, each pixels are made with RGBA(Red, Green, Blue, Alpha) value ranging from 0 to 255.</p>

<p>2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?</p>
<h3><i>Answer</i></h3>

```
from PIL import ImageColor
a = ImageColor.getcolor('CornflowerBlue', 'RGBA')
print(a)
```

<p>3. What is a box tuple?</p>
<h3><i>Answer</i></h3>
<p>Box Tuple (5,3,8,4) means the pixel start from 5 as x coordinate and 3 as y coordinate and ends at 7 as x coordinate and 3 asy coordinate.</p>

<p>4. What function returns an Image object for, say, an image file named zophie.png?</p>
<h3><i>Answer</i></h3>

```
from PIL import Image
Img = Image.open('zophie.png')
```

<p>5. How can you find out the width and height of an Image object’s image?</p>
<h3><i>Answer</i></h3>

```
from PIL import Image
Img = Image.open('zophie.png')
width, height = Img.size
print("Width of the Image is", width, "Height of the Image is", height)
```

<p>6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?</p>
<h3><i>Answer</i></h3>

```
from PIL import Image
Img = Image.open('zophie.png')
croppedImg = Img.crop((0, 50, 50, 50))
croppedImg.save('croppedImg.png')
```

<p>7. After making changes to an Image object, how could you save it as an image file?</p>
<h3><i>Answer</i></h3>

```
Imgobj.save()
```

<p>8.What module contains Pillow’s shape-drawing code?</p>
<h3><i>Answer</i></h3>

``
from PIL import Image, ImageDraw
``

<p>9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?</p>
<h3><i>Answer</i></h3>
<p>It has methods like points, lines, rectangles, ellipses and polygons.</p>
