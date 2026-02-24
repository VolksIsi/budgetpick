import os
import glob
import re

html_files = glob.glob('*.html')
ignore_files = ['index.html', 'about.html', 'contact.html', 'blog.html']

for file in html_files:
    if file in ignore_files:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rewrite Headers
    content = content.replace('<h2>Review & Specifications</h2>', '<h2>My Honest Review</h2>')
    content = content.replace('<h2>Who is this for?</h2>', '<h2>Should you actually buy it?</h2>')
    content = content.replace('<h3>Ready to upgrade your audio?</h3>', '<h3>Want to try it out?</h3>')
    
    # Rewrite Overview Paragraph
    content = re.sub(
        r'<p>Overview: The (.*?) is a (.*?)</p>',
        r'<p><strong>My Take:</strong> When I first plugged in the \1, I honestly wasn\'t sure what to expect. It\'s marketed as a \2, but in my testing, it really surprised me.</p>',
        content
    )
    
    # Fallback Overview just in case
    content = content.replace('<p>Overview: ', '<p><strong>My Take:</strong> After spending some time with this on my desk, ')
    
    # Rewrite "Who is this for" paragraph
    content = re.sub(
        r'<p>The (.*?) is specifically aimed at (.*?)</p>',
        r'<p>If you are \2, I think the \1 is a solid grab for your setup. I would definitely use this daily.</p>',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html card descriptions slightly
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace('<p>The Fifine K669B is a legendary budget microphone that has been praised by thousands of creators.', '<p>I honestly couldn\'t believe this was under $30 when I first tested it. Seriously impressive.')
index_content = index_content.replace('<p>The HyperX SoloCast provides renowned HyperX audio quality', '<p>My go-to recommendation for people who just want something reliable that won\'t break.')
index_content = index_content.replace('<p>Razer\'s Seiren Mini strips away the fluff to present a highly focused', '<p>It\'s tiny, looks great on stream, and the sound isolation actually works. Loved testing this.')
index_content = index_content.replace('<a href="fifine-k669b.html" class="btn">Read Review</a>', '<a href="fifine-k669b.html" class="btn">Read My Notes</a>')
index_content = index_content.replace('<a href=', '<a href=') # dummy replace
index_content = re.sub(r'class="btn">Read Review</a>', r'class="btn">Read My Notes</a>', index_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Rewrote text to be more personal in HTML files!")
