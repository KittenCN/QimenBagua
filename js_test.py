import js2py

context = js2py.EvalJs()
with open(f'js\iztro.min.js', 'r', encoding='utf-8') as file:
    js_content = file.read()
context.execute(js_content)