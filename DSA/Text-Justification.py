class Solution(object):
    def fullJustify(self, words, maxWidth):
        output = []
        templist = []
        curr_len = 0

        for word in words:
            if curr_len + len(word) + len(templist) > maxWidth:
                total_spaces = maxWidth - sum(len(w) for w in templist)
                if len(templist) == 1:
                    line = templist[0] + ' ' * (maxWidth - len(templist[0]))
                else:
                    gaps = len(templist) - 1
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = ""
                    for i, w in enumerate(templist):
                        line += w
                        if i < gaps:
                            line += ' ' * space_per_gap
                            if i < extra_spaces:
                                line += ' '
                output.append(line)
                templist = []
                curr_len = 0

            templist.append(word)
            curr_len += len(word)

        # Last line (left-aligned)
        last_line = ' '.join(templist)
        last_line += ' ' * (maxWidth - len(last_line))
        output.append(last_line)

        return output
