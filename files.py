# zip - crate a list of a tuple where we can fetch objects form the files/list
# if you want to up the file then useing "." can be useful e.g. ../file/doc.txt

contents = ["All things matters when it's about your family.", "Have fun at every step of the way.", "Nothing can be done."]
filenames = ["doc.txt", "present.txt", "things.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filenames}', "w")
    file.write(content)
