from docxtpl import DocxTemplate

context = { 'boss' : "И.И.Петров"}


def doc_render(context, shablon, final):
    doc = DocxTemplate(shablon)
    doc.render(context)
    doc.save(final)

doc_render(context,"ex.docx","ex-final.docx")


