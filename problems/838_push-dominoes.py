# 838. Push Dominoes
#
# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
# - dominoes[i] = 'L', if the ith domino has been pushed to the left,
# - dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# - dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        forces = [0 for _ in dominoes]

        force = 0
        for i in range(N):
            match dominoes[i]:
                case "R":
                    force = N
                case "L":
                    force = 0
                case ".":
                    force = max(force - 1, 0)

            forces[i] += force

        force = 0
        for i in range(N - 1, -1, -1):
            match dominoes[i]:
                case "L":
                    force = N
                case "R":
                    force = 0
                case ".":
                    force = max(force - 1, 0)

            forces[i] -= force

        def _result_domino(force: int) -> str:
            match force:
                case 0:
                    return "."
                case _ if force < 0:
                    return "L"
                case _ if force > 0:
                    return "R"

        result = "".join(_result_domino(f) for f in forces)
        return result


assert Solution().pushDominoes("RR.L") == "RR.L"
assert Solution().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
