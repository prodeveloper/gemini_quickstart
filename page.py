from PyPDF2 import PdfReader
import google.generativeai as genai
import os
import dbm
from dotenv import load_dotenv
from PyPDF2 import PdfReader
load_dotenv()

class SmartPDFPage:

    def __init__(self,pdf_path, page_num: int):
        self.page_num = page_num
        self.pdf_path = pdf_path
        self.extract_text()
    
        

    def setup_genai(self):
        GOOGLE_API_KEY = os.getenv('GEMINI_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model= genai.GenerativeModel('gemini-1.5-flash')
    def extract_text(self):
        reader = PdfReader(self.pdf_path)
        page = reader.pages[self.page_num]
        self.text = page.extract_text()
        
    def mece_list(self):
        prompt = "Please put this content as a mece list:"  + self.text
        response = self.get_model_response(prompt)
        return response
    def key_points(self):
        prompt = "Please put this content as a bullet point list:" + self.text
        response = self.get_model_response(prompt)
        return response
    def summary(self):
        prompt = "Please put this content as a bullet point list:" + self.text
        response = self.get_model_response(prompt)
        return response
    
    def get_model_response(self, prompt):
        cached_response = self.get_from_cache(prompt)
        if cached_response:
            return cached_response
        self.setup_genai()
        response = self.model.generate_content(prompt)
        self.save_to_cache(prompt, response.text)
        return response.text
    def get_from_cache(self,prompt:str):
        key = prompt.encode('utf-8')
        with dbm.open('smartpdf.db', 'c') as db:
            if key in db:
                content = db[key]
                return content.decode('utf-8')
            else:
                return None
    def save_to_cache(self,prompt:str, response:str):
        key = prompt.encode('utf-8')
        value = response.encode('utf-8')
        with dbm.open('smartpdf.db', 'c') as db:
            db[key] = value


    
    