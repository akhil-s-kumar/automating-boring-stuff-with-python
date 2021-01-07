<h2>Answers for the practice questions from chapter 12</h2>

<p>1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.</p>
<h3><i>Answer</i></h3>
<p>webbrowser module is used to open webpages using webbrowser.open function, requests module is used to download web pages using requests.get function and selenium module is used to automate the browser tasks.</p>

```
import webbrowser
webbrowser.open("https://google.com/")
```

```
import requests
a = requests.get("https://google.com/")
print(a.text[:1000])
```

<p>2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?</p>
<h3><i>Answer</i></h3>
<p>requests.get function will returns type 'requests.models.Response' and a.text[:1000] as a string.</p>

<p>3. What requests method checks that the download worked?</p>
<h3><i>Answer</i></h3>
<p>a.raise_for_status()</p>

<p>4. How can you get the HTTP status code of a requests response?</p>
<h3><i>Answer</i></h3>
<p>a.status_code</p>

<p>5. How do you save a requests response to a file?</p>
<h3><i>Answer</i></h3>

```
import requests
a = requests.get("https://google.com/")
saveFile = open('clone.txt', 'wb')
for i in a.iter_content(100000):
    saveFile.write(i)
```

<p>6. What is the keyboard shortcut for opening a browser’s developer tools?</p>
<h3><i>Answer</i></h3>
<p>Ctrl+Shift+C</p>

<p>7. How can you view (in the developer tools) the HTML of a specific element on a web page?</p>
<h3><i>Answer</i></h3>
<p>Hover the element then right click and click on inspect element.</p>

<p>8. What is the CSS selector string that would find the element with an id attribute of main?</p>
<h3><i>Answer</i></h3>
<po>'#main'</p>

<p>9. What is the CSS selector string that would find the elements with a CSS class of highlight?</p>
<h3><i>Answer</i></h3>
<p>'.heightlight'</p>

<p>10. What is the CSS selector string that would find all the <div> elements inside another <div> element?</p>
<h3><i>Answer</i></h3>
<p>'div div'</p>

<p>11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?</p>
<h3><i>Answer</i></h3>
<p>'button[value="favorite"]'</p>

<p>12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?</p>
<h3><i>Answer</i></h3>
<p>spam.getText()</p>

<p>13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?</p>
<h3><i>Answer</i></h3>
<p>linkElem.attrs</p>

<p>14. Running import selenium doesn’t work. How do you properly import the selenium module?</p>
<h3><i>Answer</i></h3>
<p>from selenium import webdriver</p>

<p>15. What’s the difference between the find_element_* and find_elements_* methods?</p>
<h3><i>Answer</i></h3>
<p>find_element_* returns first element as an object whereas find_elements_* returns all elements as an object</p>

<p>16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?</p>
<h3><i>Answer</i></h3>
<p>click() and send_keys()</p>

<p>17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?</p>
<h3><i>Answer</i></h3>
<p>using submit() function</p>

<p>18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?</p>
<h3><i>Answer</i></h3>
<p>forward(), back(), and refresh()</p>
