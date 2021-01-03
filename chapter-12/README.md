<h2>Answers for the practice questions from chapter 12</h2>

<p>1. webbrowser module is used to open webpages using webbrowser.open function, requests module is used to download web pages using requests.get function and selenium module is used to automate the browser tasks.</p>

```
import webbrowser
webbrowser.open("https://google.com/")
```

```
import requests
a = requests.get("https://google.com/")
print(a.text[:1000])
```

<p>2. requests.get function will returns type 'requests.models.Response' and a.text[:1000] as a string.</p>

<p>3. a.raise_for_status()</p>

<p>4. a.status_code</p>

<p>5. </p>

```
import requests
a = requests.get("https://google.com/")
saveFile = open('clone.txt', 'wb')
for i in a.iter_content(100000):
    saveFile.write(i)
```

<p>6. Ctrl+Shift+C</p>

<p>7. Hover the element then right click and click on inspect element.</p>

<po>8. '#main'</p>

<p>9. '.heightlight'</p>

<p>10. 'div div'</p>

<p>11. 'button[value="favorite"]'</p>

<p>12. spam.getText()</p>

<p>13. linkElem.attrs</p>

<p>14. from selenium import webdriver</p>

<p>15. find_element_* returns first element as an object whereas find_elements_* returns all elements as an object</p>

<p>16. click() and send_keys()</p>

<p>17. using submit() function</p>

<p>18. forward(), back(), and refresh()</p>
