# https://leetcode.com/problems/reorder-data-in-log-files/

def reorderLogFiles(logs):
        
        alpha = []
        numeric = []

        for log in logs:
            
            (header, content) = log.split(' ', 1)

            if content[0].isalpha():
                alpha.append((content, header))
            elif content[0].isnumeric():
                numeric.append(log)
        
        alpha.sort()

        return [header + " " + content for content, header in alpha] + numeric


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs2 = ["1 n u", "r 527", "j 893", "6 14", "6 82"]


print(reorderLogFiles(logs2))

