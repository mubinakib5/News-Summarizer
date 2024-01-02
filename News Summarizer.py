import tkinter as tk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    authors.config(state='normal')
    publication.config(state='normal')
    orig_summary.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', ", ".join(article.authors))

    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date))

    orig_summary.delete('1.0', 'end')
    orig_summary.insert('1.0', article.text)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    authors.config(state='disabled')
    publication.config(state='disabled')
    orig_summary.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

def clear():
    # Clear all sections
    title.config(state='normal')
    title.delete('1.0', 'end')
    title.config(state='disabled')

    authors.config(state='normal')
    authors.delete('1.0', 'end')
    authors.config(state='disabled')

    publication.config(state='normal')
    publication.delete('1.0', 'end')
    publication.config(state='disabled')

    orig_summary.config(state='normal')
    orig_summary.delete('1.0', 'end')
    orig_summary.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.config(state='disabled')

    sentiment.config(state='normal')
    sentiment.delete('1.0', 'end')
    sentiment.config(state='disabled')

    utext.delete('1.0', 'end')

# GUI SETUP
root = tk.Tk()
root.title('News Article Summarizer')
root.geometry('1024x720')

# Title, Author, Publishing Date
labels_frame = tk.Frame(root)
labels_frame.pack(pady=10)

tlabel = tk.Label(labels_frame, text='Title', font=('Helvetica', 12, 'bold'))
tlabel.grid(row=0, column=0, padx=5)

# Title Textbox
title = tk.Text(labels_frame, height=1, width=100)
title.config(state='disabled', bg='#dddddd')
title.grid(row=1, column=0)

alabel = tk.Label(labels_frame, text='Author', font=('Helvetica', 12, 'bold'))
alabel.grid(row=2, column=0, padx=5)

# Author Textbox
authors = tk.Text(labels_frame, height=1, width=100)
authors.config(state='disabled', bg='#dddddd')
authors.grid(row=3, column=0)

plabel = tk.Label(labels_frame, text='Publishing Date', font=('Helvetica', 12, 'bold'))
plabel.grid(row=4, column=0, padx=5)

# Publishing Date Textbox
publication = tk.Text(labels_frame, height=1, width=100)
publication.config(state='disabled', bg='#dddddd')
publication.grid(row=5, column=0)

# Original News and Summary
split_frame = tk.Frame(root)
split_frame.pack(expand=True, fill=tk.BOTH, pady=10)

orig_summary_label = tk.Label(split_frame, text='Original News', font=('Helvetica', 12, 'bold'))
orig_summary_label.pack(side=tk.LEFT)

summary_label = tk.Label(split_frame, text='Summary', font=('Helvetica', 12, 'bold'))
summary_label.pack(side=tk.RIGHT)

# Original News Textbox with Scrollbar
orig_summary_scrollbar = tk.Scrollbar(split_frame, orient=tk.VERTICAL)
orig_summary_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

orig_summary = tk.Text(split_frame, height=20, width=50, wrap=tk.WORD, yscrollcommand=orig_summary_scrollbar.set)
orig_summary.config(state='disabled', bg='#dddddd')
orig_summary.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

orig_summary_scrollbar.config(command=orig_summary.yview)

summary = tk.Text(split_frame, height=20, width=50, wrap=tk.WORD)
summary.config(state='disabled', bg='#dddddd')
summary.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Sentiment and URL
labels_frame_2 = tk.Frame(root)
labels_frame_2.pack(pady=10)

selabel = tk.Label(labels_frame_2, text='Sentiment', font=('Helvetica', 12, 'bold'))
selabel.grid(row=0, column=0, padx=5)

# Sentiment Textbox
sentiment = tk.Text(labels_frame_2, height=1, width=100)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.grid(row=1, column=0)

ulabel = tk.Label(labels_frame_2, text='URL', font=('Helvetica', 12, 'bold'))
ulabel.grid(row=2, column=0, padx=5)

# URL Textbox
utext = tk.Text(labels_frame_2, height=1, width=100)
utext.grid(row=3, column=0)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn = tk.Button(btn_frame, text='Summarize', command=summarize)
btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(btn_frame, text='Clear', command=clear)
clear_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()