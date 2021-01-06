<h2>Answers to the Practice Questions from chapter 20</h2>

<p>1. How can you trigger PyAutoGUI’s fail-safe to stop a program?</p>
<h3><i>Answer</i></h3>
<p>Move the mouse to the any of the 4 corners.</p>

<p>2. What function returns the current resolution()?</p>
<h3><i>Answer</i></h3>

```
import pyautogui
size = pyautogui.size() 
print(size)
```

<p>3. What function returns the coordinates for the mouse cursor’s current position?</p>
<h3><i>Answer</i></h3>

```
import pyautogui
a = pyautogui.position()
print(a)
```

<p>4. What is the difference between pyautogui.moveTo() and pyautogui.move()?</p>
<h3><i>Answer</i></h3>
<p>pyautogui.moveTo() will move the mouse to absolute coordinate of the screen and pyautogui.move() will move the mouse with respect to the current position of mouse. </p>

<p>5. What functions can be used to drag the mouse?</p>
<h3><i>Answer</i></h3>

```
pyautogui.dragTo()
pyautogui.drag()
```

<p>6. What function call will type out the characters of "Hello, world!"?</p>
<h3><i>Answer</i></h3>

```
pyautogui.write('Hello, world!')
```

<p>7. How can you do keypresses for special keys such as the keyboard’s left arrow key?</p>
<h3><i>Answer</i></h3>

```
pyautogui.write(['left'])
```

<p>8. How can you save the current contents of the screen to an image file named screenshot.png?</p>
<h3><i>Answer</i></h3>

```
import pyautogui
pyautogui.screenshot('screenshot.png')
```

<p>9. What code would set a two-second pause after every PyAutoGUI function call?</p>
<h3><i>Answer</i></h3>

```
pyautogui.sleep(3)
```

<p>10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?</p>
<h3><i>Answer</i></h3>
<p>Selenium</p>

<p>11. What makes PyAutoGUI error-prone?</p>
<h3><i>Answer</i></h3>
<p></p>

<p>12. How can you find the size of every window on the screen that includes the text Notepad in its title?</p>
<h3><i>Answer</i></h3>

```
pyautogui.getWindowsWithTitle('Notepad')
```

<p>13. How can you make, say, the Firefox browser active and in front of every other window on the screen?</p>
<h3><i>Answer</i></h3>
<p></p>
