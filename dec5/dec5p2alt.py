import copy
from dataclasses import dataclass
from typing import Optional
import re
from dataclasses import dataclass
from functools import wraps
from importlib import import_module
import os
from pathlib import Path
from typing import Callable, Optional

TestData = list[str] | str

@dataclass
class RegistryEntry:
  year: int
  day: int
  part: int
  solution: Callable[[list[str]], any]
  test: Optional[tuple[TestData, any]] = None

SOLUTION_REGISTRY: dict[str, RegistryEntry] = {}

def get_registry_key(year: int, day: int, part: int) -> str:
  return f"{year}:{day}:{part}"

def register(year: int, day: int, part: int, *, test: Optional[tuple[list[str], any]] = None):
  def outer(f):
    SOLUTION_REGISTRY[get_registry_key(year, day, part)] = RegistryEntry(year, day, part, f, test)
    
    @wraps(f)
    def inner(data: list[str]):
      return f(data)
    
    return inner
  
  return outer

def import_all_solutions(root: str):
    """Automatically import all solutions in the project"""
    root_path = Path(root)
    days = sorted(root_path.rglob("year_*/*.py"))

    for day in days:
        import_module(f"adventofcode.{day.parent.name}.{os.path.splitext(day.name)[0]}")


def ints(input: str) -> list[int]:
  return [int(match) for match in re.findall(r"\d+", input)]

def digits(input: str) -> list[int]:
  return [int(match) for match in re.findall(r"\d", input)]


test_almanac ="""
seeds: 79 14 55 13

seed-to-soil map:
50 80 5
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

"""

    
    

@dataclass
class AlmanacMapping:
  dest_start: int
  source_start: int
  length: int
  
  @classmethod
  def from_str(cls, text: str):
    nums = ints(text)
    return cls(*nums)
  
  def contains(self, x: int) -> bool:
    return x >= self.source_start and x < self.source_start + self.length
  
  def map(self, x: int) -> int:
    offset = x - self.source_start
    
    if offset >= self.length:
      raise Exception(f"Index {x} is out of bounds")
    
    return self.dest_start + offset


@dataclass
class AlmanacRange:
  start: int
  length: int
  
  def split(self, split_point: int) -> tuple['AlmanacRange', 'AlmanacRange']:
    end = self.start + self.length
    first = AlmanacRange(self.start, split_point - self.start)
    second = AlmanacRange(split_point, end - split_point)
    return first, second
  
  def apply_mapping(self, mapping: AlmanacMapping):
    offset = mapping.dest_start - mapping.source_start
    self.start += offset
  
  def is_inside(self, mapping: AlmanacMapping):
    map_start, map_end = mapping.source_start, mapping.source_start + mapping.length
    start, end = self.start, self.start + self.length
    
    return (start >= map_start and end <= map_end)
  
  def overlap_point(self, mapping: AlmanacMapping) -> Optional[int]:
    map_start, map_end = mapping.source_start, mapping.source_start + mapping.length
    start, end = self.start, self.start + self.length
    
    right_edge_overlap = (end > map_start and end <= map_end)
    left_edge_overlap = (start < map_end and start >= map_start)
    
    if right_edge_overlap:
      return map_start
    elif left_edge_overlap:
      return map_end
    
    return None
  
  def overlaps(self, mapping: AlmanacMapping) -> bool:
    map_start, map_end = mapping.source_start, mapping.source_start + mapping.length
    start, end = self.start, self.start + self.length
    
    overlaps = (end > map_start and end <= map_end) or (start < map_end and start >= map_start)
    
    return overlaps
    

@dataclass
class Almanac:
  seeds: list[int]
  mappings: list[list[AlmanacMapping]]
  
  @classmethod
  def from_text(cls, text: str):
    groups = text.split("\n\n")
  
    seeds = ints(groups[0])
        
    mappings = []
    for group in groups[1:]:
      mapping_group = [AlmanacMapping.from_str(line) for line in group.split("\n")[1:]]
      mappings.append(mapping_group)
    
    return cls(seeds, mappings)
  
  def lookup_location(self, seed: int) -> int:
    num = seed
    for category in self.mappings:
      # linear search - could optimize with binary search + sorting
      for mapping in category:
        if mapping.contains(num):
          num = mapping.map(num)
          break
    
    return num
  
  
@dataclass
class AlmanacV2:
  seeds: list[AlmanacRange]
  mappings: list[list[AlmanacMapping]]
  
  @classmethod
  def from_text(cls, text: str):
    groups = text.split("\n\n")
            
    seeds = []
    nums = ints(groups[0])
    for idx in range(0, len(nums), 2):
      seeds.append(AlmanacRange(nums[idx], nums[idx+1]))
    
    mappings = []
    for group in groups[1:]:
      mapping_group = [AlmanacMapping.from_str(line) for line in group.split("\n")[1:]]
      mappings.append(mapping_group)
    
    return cls(seeds, mappings)
  
  
  def lookup_locations(self) -> list[AlmanacRange]:
    alm_ranges = [copy.copy(seed) for seed in self.seeds]
    map_queue = alm_ranges
    next_category = []
    for category in self.mappings:
      while len(map_queue) > 0:
        alm_range = map_queue.pop()
        found_overlap = False
        
        for mapping in category:
          if not alm_range.overlaps(mapping):
            continue
          found_overlap = True
          if alm_range.is_inside(mapping):
            alm_range.apply_mapping(mapping)
            next_category.append(alm_range)
          else:
            split_ranges = alm_range.split(alm_range.overlap_point(mapping))
            map_queue.extend(split_ranges)
          break
            
        if not found_overlap:
          next_category.append(alm_range)
          
      map_queue = next_category
      next_category = []
    
    return map_queue
    

@register(2023, 5, 1, test=(test_almanac, 35))
def part_one(lines: list[str]):
  all_text = "\n".join(lines)
  almanac = Almanac.from_text(all_text)
  locations = [almanac.lookup_location(seed) for seed in almanac.seeds]
  return min(locations)

@register(2023, 5, 2, test=(test_almanac, 46))
def part_two(test_almanac):
  all_text = test_almanac
  almanac = AlmanacV2.from_text(all_text)
  locations = almanac.lookup_locations()
  return min(alm_range.start for alm_range in locations)

print(part_two(test_almanac))