from PyPDF2 import PdfReader
import dbm
from PyPDF2 import PdfReader

class SmartPDFPage:

    def __init__(self,pdf_path, page_num: int, model=None):
        self.page_num = page_num
        self.pdf_path = pdf_path
        self.model = model
        self.text = None
        self.extract_text()

    def extract_text(self):
        if self.text is None:
            reader = PdfReader(self.pdf_path)
            page = reader.pages[self.page_num]
            self.text = page.extract_text()
        return self.text
        
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
        breakpoint()
        response = self.get_model_response(prompt)
        return response
    
    def get_model_response(self, prompt):
        cached_response = self.get_from_cache(prompt)
        if cached_response:
            return cached_response
        response = self.model.generate_content(prompt)
        self.save_to_cache(prompt, response.text)
        return response.text
    def get_from_cache(self,prompt:str):
        key = prompt.encode('utf-8')
        with dbm.open('cache.db', 'c') as db:
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


    
    