# SPDX-License-Identifier: Apache-2.0

# First Party
from instructlab.sdg.registry import BlockRegistry
from instructlab.sdg.blocks.block import Block
from datasets import Dataset
import yaml
import json


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
                "keywords": None,
                "named_entities": {
                    "organizations": None,
                    "people": None,
                    "locations": None,
                    "dates": None,
                },
                "sentiment": sample.get("sentiment", None),
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
