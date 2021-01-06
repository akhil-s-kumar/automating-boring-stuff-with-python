<h2>Answers to the Practice Questions from chapter 10</h2>

<p>1. What is the difference between shutil.copy() and shutil.copytree()?</p>
<h3><i>Answer</i></h3>
<p>shutil.copytree() creates a backup for the original project whereas shutil.copy() will copy a single file.</p>

<p>2. What function is used to rename files?</p>
<h3><i>Answer</i></h3>

```
shutil.move()
```

<p>3. What is the difference between the delete functions in the send2trash and shutil modules?</p>
<h3><i>Answer</i></h3>
<p>send2trash functions will move file or folder to the recycle bin whereas shutil functions will permanently delete files and folders.</p>

<p>4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?</p>
<h3><i>Answer</i></h3>

```
zipfile.ZipFile()
```
