# SPDX-License-Identifier: Apache-2.0

# First Party
from instructlab.sdg.registry import BlockRegistry
from instructlab.sdg.blocks.block import Block
from datasets import Dataset


@BlockRegistry.register("AddStaticValue")
class AddStaticValue(Block):
    def __init__(self, ctx, pipe, block_name, column_name: str, static_value: str):
        super().__init__(ctx, pipe, block_name)
        self.column_name = column_name
        self.static_value = static_value

    # Using a static method to avoid serializing self when using multiprocessing
    @staticmethod
    def _map_populate_column(samples, column_name, static_value, num_proc=1):
        def populate_column(sample):
            sample[column_name] = static_value
            return sample

        return samples.map(populate_column, num_proc=num_proc)

    def generate(self, samples: Dataset) -> Dataset:
        samples = self._map_populate_column(
            samples, self.column_name, self.static_value
        )
        return samples
