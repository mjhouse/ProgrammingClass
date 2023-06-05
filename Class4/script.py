#!/usr/bin/env python

import requests

from pypdf import PdfReader, PdfWriter

def main():
    reader = PdfReader("scratch/document.pdf")
    fields = reader.get_form_text_fields()

    # for key, value in fields.items():
    #     print(f"{key} = {value}")

    fields["NewSoftware-version"] = 290

    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    for page in writer.pages:
        writer.update_page_form_field_values(page,fields)

    writer.write("scratch/output.pdf")

if __name__=='__main__':
    main()