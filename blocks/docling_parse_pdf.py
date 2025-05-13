# SPDX-License-Identifier: Apache-2.0

# First Party
from instructlab.sdg.registry import BlockRegistry
from instructlab.sdg.blocks.block import Block
from datasets import Dataset
from docling.document_converter import DocumentConverter


@BlockRegistry.register("DoclingParsePDF")
class DoclingParsePDF(Block):
    def __init__(self, ctx, pipe, block_name, pdf_path_column: str, output_column: str):
        super().__init__(ctx, pipe, block_name)
        self.pdf_path_column = pdf_path_column
        self.output_column = output_column
        self.converter = DocumentConverter()

    @staticmethod
    def _map_parse_pdf(samples, pdf_path_column, output_column, converter, num_proc=1):
        def parse_pdf(sample):
            pdf_path = sample[pdf_path_column]
            result = converter.convert(pdf_path)
            sample[output_column] = result.document.export_to_markdown()
            return sample

        return samples.map(parse_pdf, num_proc=num_proc)

    def generate(self, samples: Dataset) -> Dataset:
        samples = self._map_parse_pdf(
            samples, self.pdf_path_column, self.output_column, self.converter
        )
        return samples
