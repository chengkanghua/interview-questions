import re

html_source = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
</html>
"""

# 使用正则表达式匹配charset属性
match = re.search(r'<meta charset="([^"]*)"', html_source)
if match:
    encoding = match.group(1)
    print(f"HTML source encoding is: {encoding}")
else:
    print("No encoding found in HTML source.")