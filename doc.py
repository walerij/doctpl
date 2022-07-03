from docxtpl import DocxTemplate
doc = DocxTemplate("ex.docx")
context = { 'boss' : "И.И.Петров"}
doc.render(context)
doc.save("ex-final.docx")