#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ''):
      self.value = value

  @property
  def value(self):
      return self._value

  @value.setter
  def value(self, value):
      if isinstance(value, str):
        self._value = value
      else:
        print("The value must be a string.")

  def is_sentence(self):
      return self.value.endswith(".")

  def is_question(self):
      return self.value.endswith("?")

  def is_exclamation(self):
      return self.value.endswith("!")

  def count_sentences(self):
      return len([word for word in self.value.split() if word.endswith((".", "?", "!"))])