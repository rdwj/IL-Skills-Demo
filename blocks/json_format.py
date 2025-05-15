# SPDX-License-Identifier: Apache-2.0

# First Party
from instructlab.sdg.registry import BlockRegistry
from instructlab.sdg.blocks.block import Block
from datasets import Dataset
import yaml
import json
import re

def replace_unicode_escape_sequences(text):
    replacements = {
        '\u00a1': '¡',  # ¡ (inverted exclamation mark)
        '\u00ac': '¡Á',  # Á (capital A with acute accent)
        '\u00ab': '¡À',  # À (lowercase A with acute accent)
        '\u00ae': '¡ä',  # ä (lowercase e with acute accent)
        '\u00af': '¡â',  # â (lowercase a with circumflex accent)
        '\u00b1': '¡£',  # £ (pound sign, used in Spanish currency notation)
        '\u00bb': '¡¿',  # ¿ (inverted question mark)
        '\u00bc': '¡“',  # “ ( quotation mark with guillemet)
        '\u00bd': '¡’',  # ‘ ( apostrophe)
        '\u00be': '¡’',  # ‟ (single quotation mark with guillemet)
        '\u00bf': '¡»',  # » (right-pointing single quote)
        '\u00c0': 'Á',  # á (lowercase A with acute accent)
        '\u00c1': 'À',  # à (upper case A with acute accent)
        '\u00e0': 'ä',  # ä (lowercase e with acute accent)
        '\u00e1': 'â',  # â (lowercase a with circumflex accent)
        '\u00f1': 'ñ',  # ñ (n with tilde, used in Spanish lettering)
        '\u00d8': '',  # 8 (eight, sometimes represented as a digraph with a tilde in Spanish typography)
    }
    for key, value in replacements.items():
        text = re.sub(key, value, text, flags=re.IGNORECASE)
    return text

@BlockRegistry.register("JSONFormat")
class JSONFormat(Block):
    def __init__(self, ctx, pipe, block_name, output_column: str):
        super().__init__(ctx, pipe, block_name)
        self.output_column = output_column

    @staticmethod
    def _parse_named_entities(raw_text):
        try:
            parsed = yaml.safe_load(raw_text)
            return {
                "organizations": parsed.get("organizations", [])
                if isinstance(parsed, dict)
                else [],
                "people": parsed.get("people", []) if isinstance(parsed, dict) else [],
                "locations": parsed.get("locations", [])
                if isinstance(parsed, dict)
                else [],
                "dates": parsed.get("dates", []) if isinstance(parsed, dict) else [],
            }
        except Exception:
            return {
                "organizations": None,
                "people": None,
                "locations": None,
                "dates": None,
            }

    @staticmethod
    def _map_format_json(samples, output_column, num_proc=1):
        def format_json(sample):
            json_output = {
                "summary": sample.get("summary", None),
                "tldr": sample.get("tldr", None),
                "keywords": None,
                "named_entities": {
                    "organizations": None,
                    "people": None,
                    "locations": None,
                    "dates": None,
                },
                "sentiment": sample.get("sentiment", None),
                "seo": json.loads(sample.get("seo", None)),
                "summary_es": replace_unicode_escape_sequences(sample.get("summary_es", None)),
                # "intention": json.loads(sample.get("intention", None)), # Added for homework assignment.
            }

            try:
                if isinstance(sample.get("keywords"), str):
                    json_output["keywords"] = [
                        kw.strip() for kw in sample["keywords"].split(",") if kw.strip()
                    ]
            except Exception:
                json_output["keywords"] = None

            try:
                if isinstance(sample.get("named_entities"), str):
                    json_output["named_entities"] = JSONFormat._parse_named_entities(
                        sample["named_entities"]
                    )
            except Exception:
                json_output["named_entities"] = None

            sample[output_column] = json.dumps(json_output)
            return sample

        return samples.map(format_json, num_proc=num_proc)

    def generate(self, samples: Dataset) -> Dataset:
        samples = self._map_format_json(samples, self.output_column)
        return samples
