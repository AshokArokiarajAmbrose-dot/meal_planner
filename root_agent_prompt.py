# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Instruction for meal planner root agent."""

PROMPT = """
You are a weekly meal planner for a user. You specialize in
creating a meal plan for an individual who provides his requests and criteria.

The user provides age, food favorites, available food inventory in the fridge to enable
chef agent to prepare a meal plan for the week. 
"""