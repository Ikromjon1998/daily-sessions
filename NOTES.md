# Notes

One entry per exercise: what I learned.

- two-fer: 
- black-jack: tuples pack/unpack with commas; each function defines its own ace rule; return conditions directly, not if/True/False.
- collatz-conjecture: guard clause first, then loop; `//` keeps ints, `/` returns float; ternary replaces if/else assignment.
- little-sisters-vocab: strings, slices, and list comprehensions.
  - `join` only puts the separator *between* items. It does not change them.
    My first try was `'::'.join(words)` and the words came back unchanged.
    To add a prefix to each word I had to build a new list first, with a
    list comprehension: `[prefix + word for word in words[1:]]`.
  - A slice has three slots: `[start:stop:step]`. I wrote `word[::-3]`, which
    means "step backwards by 3", when I meant `word[:-4]`, "stop 4 from the
    end". Rule of thumb: two colons means the last number is a step.
  - `word.removesuffix('ness')` says what it means, so it beats `word[:-4]`.
  - Negative indexes just work: `words[-1]` is the last word. No length maths.
  - `strip('.')` removes the character when it is there and does nothing when
    it is not, so it can replace a whole if/else.
  - Clean-up pass, after the tests were already green:
    - `from typing import List` is the old way. Since Python 3.9 the builtin
      works as a type: `list[str]`, and there is nothing to import.
    - Leaving one parameter untyped made mypy call my *return value* `Any`,
      even though I had annotated the return as `-> str`. One missing hint
      spreads to everything downstream of it.
    - My long line was 94 characters because it repeated `words[index]` three
      times. Swapping the if/else for `.strip('.')` took it to 41. The fix was
      deleting the branch, not wrapping the line.
