import codewars_test as test

# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
'''


def unique_in_order(sequence):
    unique_sequence = []
    for item in sequence:
        if not unique_sequence or item != unique_sequence[-1]:
            unique_sequence.append(item)
    return unique_sequence


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Should work with empty sequence")
    def _():
        test.assert_equals(unique_in_order(""), [])
        test.assert_equals(unique_in_order([]), [])
        test.assert_equals(unique_in_order(()), [])

    @test.it("Should work with single element sequence")
    def _():
        test.assert_equals(unique_in_order("A"), ["A"])
        test.assert_equals(unique_in_order(["A"]), ["A"])
        test.assert_equals(unique_in_order(("A",)), ["A"])

    @test.it("Should reduce duplicates")
    def _():
        test.assert_equals(unique_in_order("AA"), ["A"])
        test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

    @test.it("Should be case-sensitive")
    def _():
        test.assert_equals(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

    @test.it("Should work with different element types")
    def _():
        test.assert_equals(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
        test.assert_equals(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])
