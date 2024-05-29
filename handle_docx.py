
# remove paragraphs using docx package
def remove_empty_paragraphs(doc):
    for para in doc.paragraphs:
        if not para.text.strip():
            p_element = para._element
            p_element.getparent().remove(p_element)



# extract_content using docx2python
def extract_content(doc):
    data_list=[]
    for sentence in doc.body[0][0][0]:
        print(sentence.strip())
        data_list.append(sentence.strip())         
    
    return data_list
def extract_footnote_pos_string(doc, footnote_string):
    for sentence in doc.body[0][0][0]:
        string = sentence.strip()
        p = string.find(footnote_string)
        if p != -1:
            pos = p
    return string[pos-10:pos]

# extract_footnote using docx2python
def extract_footnote(doc):
    footnote_list = []
    for footnote in doc.footnotes_runs[0][0]:
        for specific in footnote:
            for line in specific:
                split_lines = line.split("\t")
                if "footnote" not in split_lines[0]:                    
                    footnote_list.append(split_lines[0].strip())
    return footnote_list

# # extract_content using Document from docx
# def extract_content(doc):
#     data_list=[]
#     for paragraph in doc.paragraphs:    
#         data_list.append(paragraph.text.strip())
#     return data_list

# handle paragraph using Document from docx-python package
def remove_string_from_paragraph(doc, target_string):
    for paragraph in doc.paragraphs:            
        if target_string in paragraph.text:
            print(paragraph.text)
            paragraph.text = paragraph.text.replace(target_string, '')

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None