# 1678. Goal Parser Interpretation
#
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


assert Solution().interpret("G()(al)") == "Goal"
assert Solution().interpret("G()()()()(al)") == "Gooooal"
assert Solution().interpret("(al)G(al)()()G") == "alGalooG"
