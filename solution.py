class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, i, n = [], 0, len(words)
        while i < n:
            length, j = len(words[i]), i + 1
            while j < n and length + 1 + len(words[j]) <= maxWidth:
                length += 1 + len(words[j])
                j += 1
            gaps = j - i - 1
            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - (length - gaps)
                space, extra = divmod(total_spaces, gaps)
                line = ""
                for k in range(gaps):
                    line += words[i + k] + " " * (space + (k < extra))
                line += words[j - 1]
            res.append(line)
            i = j
        return res
