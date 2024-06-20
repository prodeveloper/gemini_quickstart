from PyPDF2 import PdfReader
import google.generativeai as genai
import dbm
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from .page import SmartPDFPage
load_dotenv()

class SmartPDF:
    def __init__(self,pdf_path, gemini_key,gemini_model='gemini-1.5-flash'):
        self.pdf_path = pdf_path
        self.gemini_key = gemini_key
        self.gemini_model = gemini_model
    
    def extract_text(self):
        reader = PdfReader(self.pdf_path)
        page = reader.pages[self.page_num]
        self.text = page.extract_text()
    
    def setup_genai(self):
        genai.configure(api_key=self.gemini_key)
        self.model= genai.GenerativeModel(self.gemini_model)
    def enable_persistent_cache(self):
        self.cache = dbm.open('smartpdf.db', 'c')
        #TODO implement cache
    def page(self, page_num: int):
        self.page_num = page_num
        self.setup_genai()
        return SmartPDFPage(self.pdf_path, self.page_num,self.model)