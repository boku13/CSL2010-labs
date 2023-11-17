# from lab import bruh2

# from collections import defaultdict

# # Function to read words from a text file and convert to lowercase
# def read_words_from_file(file_path):
#     with open(file_path, "r") as file:
#         words = file.read().lower().split()
#     return words

# # Function to identify words common in all chapters
# def get_common_words(chapters):
#     common_words = set(read_words_from_file(chapters[0]))
#     for chapter in chapters[1:]:
#         common_words.intersection_update(set(read_words_from_file(chapter)))
#     return common_words

# # Function to remove common words from each chapter
# def remove_common_words(chapters, common_words):
#     cleaned_chapters = []
#     for chapter in chapters:
#         words = read_words_from_file(chapter)
#         cleaned_words = [word for word in words if word not in common_words]
#         cleaned_chapters.append(cleaned_words)
#     return cleaned_chapters

# # Example usage
# if __name__ == "__main__":
#     # List of chapter file paths
#     chapter_files = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]

#     # Get words common in all chapters
#     common_words = get_common_words(chapter_files)
#     print("Common Words in All Chapters:", common_words)

#     # Remove common words from each chapter
#     cleaned_chapters = remove_common_words(chapter_files, common_words)

#     # Count frequencies of non-common words in each chapter
#     word_counts = defaultdict(lambda: [0] * len(chapter_files))
#     for i, chapter in enumerate(cleaned_chapters):
#         for word in chapter:
#             word_counts[word][i] += 1

#     count = 0
#     # Print non-common words along with frequencies in each chapter
#     for word, frequencies in word_counts.items():
#         print(f"{word}: {', '.join(str(freq) for freq in frequencies)}")
#         count+=1
#     print(count)

from collections import defaultdict

# Function to read words from a text file and convert to lowercase
def read_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.read().lower().split()
    return words

# Function to identify words common in all chapters
def get_common_words(chapters):
    common_words = set(read_words_from_file(chapters[0]))
    for chapter in chapters[1:]:
        common_words.intersection_update(set(read_words_from_file(chapter)))
    return common_words

# Function to remove common words from each chapter
def remove_common_words(chapters, common_words):
    cleaned_chapters = []
    for chapter in chapters:
        words = read_words_from_file(chapter)
        cleaned_words = [word for word in words if word not in common_words]
        cleaned_chapters.append(cleaned_words)
    return cleaned_chapters

# Example usage
if __name__ == "__main__":
    # List of chapter file paths
    chapter_files = ["chapter1.txt", "chapter2.txt", "chapter3.txt"]

    # Get words common in all chapters
    common_words = get_common_words(chapter_files)
    print("Common Words in All Chapters:", common_words)

    # Remove common words from each chapter
    cleaned_chapters = remove_common_words(chapter_files, common_words)

    # Count frequencies of non-common words in each chapter
    word_counts = defaultdict(lambda: [0] * len(chapter_files))
    for i, chapter in enumerate(cleaned_chapters):
        for word in chapter:
            word_counts[word][i] += 1

    count = 0
    # Print non-common words along with frequencies in each chapter in alphabetical order
    for word in sorted(word_counts.keys()):
        frequencies = word_counts[word]
        print(f"{word}: {', '.join(str(freq) for freq in frequencies)}")
        count+=1
    print(count)
    
    
this = sorted(list(word_counts.keys()))
print(this)
    
# bruh3 = list(set(bruh2).difference(this))
# print(bruh3)