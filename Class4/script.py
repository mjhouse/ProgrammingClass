#!/usr/bin/env python

import requests

from pypdf import PdfReader, PdfWriter

class PdfFiller:

    def __init__(self, path):
        self.reader = PdfReader(path)
        self.writer = PdfWriter()
        self.writer.append_pages_from_reader(self.reader)

    def read(self):
        return self.reader.get_form_text_fields()

    def write(self, fields):
        for page in self.writer.pages:
            self.writer.update_page_form_field_values(
                page,
                fields)

    def save(self, path):
        self.writer.write(path)

def main():
    form_filler = PdfFiller("scratch/document.pdf")

    fields = form_filler.read()

    for key, value in fields.items():
        print(f"{key} = {value}")

    fields["ticketnumer"] = 8675309
    fields["VendorName"] = 8675309
    fields["Prodnamefield"] = "helloworld"
    form_filler.write(fields)

    form_filler.save("scratch/output.pdf")

   
   
   
   
   
   
   
   
   
   
    # reader = PdfReader("scratch/document.pdf")
    # fields = reader.get_form_text_fields()

    # # for key, value in fields.items():
    # #     print(f"{key} = {value}")

    # fields["NewSoftware-version"] = 290

    # writer = PdfWriter()
    # writer.append_pages_from_reader(reader)

    # for page in writer.pages:
    #     writer.update_page_form_field_values(page,fields)

    # writer.write("scratch/output.pdf")

if __name__=='__main__':
    main()