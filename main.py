
from app.SmartPage.document import SmartPDF
from dotenv import load_dotenv
import os
load_dotenv()
file_path = 'app/SmartPage/sample_pdfs/map_reduce.pdf'
page_num = 1
gemini_key = os.getenv('GEMINI_KEY')
smart_doc = SmartPDF(file_path, gemini_key)
page=smart_doc.page(1)

print(page.summary())