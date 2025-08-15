from docling.datamodel.pipeline_options import PdfPipelineOptions, OcrOptions, TesseractCliOcrOptions
from docling.document_converter import DocumentConverter, ImageFormatOption
from docling.datamodel.base_models import InputFormat

# --- pipeline options for images (uses StandardPdfPipeline under the hood)
opts = PdfPipelineOptions()
opts.do_ocr = True
opts.generate_page_images = True
opts.generate_parsed_pages = True
opts.generate_table_images = True
opts.images_scale = 2.0  # bump resolution for OCR/table model

# OCR backend (prefer Tesseract CLI if available)
try:
    opts.ocr_options = TesseractCliOcrOptions(force_full_page_ocr=True)
except Exception:
    opts.ocr_options = OcrOptions()

converter = DocumentConverter(
    format_options={InputFormat.IMAGE: ImageFormatOption(pipeline_options=opts)}
)

conv = converter.convert("./1000036757.jpg")
doc = conv.document
print(doc.export_to_markdown())
