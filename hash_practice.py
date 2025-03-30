word_count = {}

with open('C:/Users/user/Downloads/hw2_data.txt', 'r') as file:
    for line in file:
        word = line.strip()
        if word:
            word_count[word] = word_count.get(word, 0) + 1

print(f"共有 {len(word_count)} 個不重複的單字")
for word, count in word_count.items():
    print(f"{word}: {count}個")

import matplotlib.pyplot as plt

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
words = [item[0] for item in sorted_word_count]
counts = [item[1] for item in sorted_word_count]

plt.figure(figsize=(12, 6))
plt.bar(words, counts, color='skyblue')
plt.xlabel('words')
plt.ylabel('counts')
plt.title('Word Frequency Bar Chart')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()