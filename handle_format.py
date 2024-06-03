# from docx import Document
# from docx.shared import Pt, RGBColor
# from docx.enum.text import WD_ALIGN_PARAGRAPH

def copy_paragraph_style(source_paragraph, target_paragraph, copy_para):

    for i, source_run in enumerate(source_paragraph.runs):   
        target_run = target_paragraph.add_run()     
        copy_run = copy_para.add_run()
        
        copy_run.text = target_paragraph.runs[i].text
        if 'https://' not in target_paragraph.runs[i].text:
            font_source = source_run.font
            font_target = copy_run.font

            font_target.name = font_source.name
            font_target.size = font_source.size
            font_target.bold = font_source.bold
            font_target.italic = font_source.italic
            font_target.underline = font_source.underline
            font_target.color.rgb = font_source.color.rgb
            font_target.highlight_color = font_source.highlight_color