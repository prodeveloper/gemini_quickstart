from page import SmartPDFPage

file_path = 'sample_pdfs/map_reduce.pdf'
page_num = 0

page = SmartPDFPage(file_path, page_num)
print(page.summary())