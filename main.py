#coding=utf-8
import re
vowels = set(u'аеёиоуыэюя')
pattern_str = u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))"

sign_chars = set(u'ъь')

word = raw_input('слово:').decode('utf-8')

mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
print mask

syllables = [word[m.start():m.end()] for m in re.finditer(pattern_str,mask)]
print '-'.join(syllables)

