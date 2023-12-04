# index.py
file = open('index.html', 'r')
html_content = file.read()
file.close()

print('Content-Type: text/html')
print('')
print(html_content)
