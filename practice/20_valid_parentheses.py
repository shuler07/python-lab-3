class Solution:
    def isValid(self, s: str) -> bool:
        rc = sc = fc = 0
        q: list[str] = []

        for char in s:
            match char:
                case "(":
                    rc += 1
                case "[":
                    sc += 1
                case "{":
                    fc += 1
                case ")":
                    if len(q) == 0 or q.pop() != "(":
                        return False
                    rc -= 1
                case "]":
                    if len(q) == 0 or q.pop() != "[":
                        return False
                    sc -= 1
                case "}":
                    if len(q) == 0 or q.pop() != "{":
                        return False
                    fc -= 1
            if char in "([{":
                q.append(char)

        if sc == rc == fc == 0:
            return True
        return False
