class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for word in sentence.split():
            if any(char.isdigit() for char in word):
                continue
            if (
                word.count("-") > 1
                or word.count("!") > 1
                or word.count(".") > 1
                or word.count(",") > 1
            ):
                continue
            if "-" in word:
                hyphen_index = word.index("-")
                if (
                    hyphen_index == 0
                    or hyphen_index == len(word) - 1
                    or not (
                        word[hyphen_index - 1].isalpha()
                        and word[hyphen_index + 1].isalpha()
                    )
                ):
                    continue
            if any(char in "!.," for char in word[:-1]):
                continue
            count += 1
        return count
