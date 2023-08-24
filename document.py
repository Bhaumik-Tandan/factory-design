"""
Document Generator Factory:
Design a DocumentGeneratorFactory that produces document generators for various formats (PDF, HTML, Markdown).
"""
from abc import ABC, abstractmethod

class DocumentGeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self, filename):
        pass

class DocumentGenerator(DocumentGeneratorFactory):
    def __init__(self, filename):
        self.filename = filename

    def display_info(self):
        pass

class PDF(DocumentGenerator):
    def display_info(self):
        print(f"This is a PDF document with filename {self.filename}")

class HTML(DocumentGenerator):
    def display_info(self):
        print(f"This is an HTML document with filename {self.filename}")

class Markdown(DocumentGenerator):
    def display_info(self):
        print(f"This is a Markdown document with filename {self.filename}")

class DocumentGeneratorFactoryImpl(DocumentGeneratorFactory):
    def create_generator(self, format_type, filename):
        if format_type == "pdf":
            return PDF(filename)
        elif format_type == "html":
            return HTML(filename)
        elif format_type == "markdown":
            return Markdown(filename)
        else:
            raise ValueError("Invalid document format")

def main():
    factory = DocumentGeneratorFactoryImpl()

    pdf_generator = factory.create_generator("pdf", "filename.pdf")
    html_generator = factory.create_generator("html", "filename.html")
    markdown_generator = factory.create_generator("markdown", "filename.md")

    generators = [pdf_generator, html_generator, markdown_generator]
    for generator in generators:
        generator.display_info()

if __name__ == "__main__":
    main()
