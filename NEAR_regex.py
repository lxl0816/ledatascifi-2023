{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c56480d-1397-4874-820a-6e57a7f35fc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def NEAR_regex(list_of_words,max_words_between=5,partial=False,cases_matter=False):\n",
    "    '''\n",
    "    Parameters\n",
    "    ----------\n",
    "    list_of_words : list\n",
    "        A list of \"words\", each element is a string\n",
    "        \n",
    "        This program will return a regex that will look for times where word1 \n",
    "        is near word2, or word2 is near word 1.\n",
    "        \n",
    "        It works with multiple words: You can see if words1 is near word2 or\n",
    "        word3. \n",
    "        \n",
    "    max_words_between : int, optional\n",
    "        How many \"words\" are allowed between words in list_of_words. The default\n",
    "        is 5, but you should consider this carefully.\n",
    "        \n",
    "        \"words\" in between are chunks of characters. \"DON don don- don12 2454\" \n",
    "        is 5 words.\n",
    "        \n",
    "        This will not allow matches if the words are separated by a newline \n",
    "        (\"\\n\") character.\n",
    "        \n",
    "    partial : Boolean, optional\n",
    "        If true, will accept longer words than you give. For example, if one \n",
    "        word in your list is \"how\", it will match to \"howdy\". Be careful in \n",
    "        choosing this based on your problem. Partial makes more sense with \n",
    "        longer words. \n",
    "        The default is True.\n",
    "        \n",
    "    cases_matter: Boolean, optional bt IMPORTANT\n",
    "        If True, will return a regex string that will only catch cases where  \n",
    "        words in the string have the same case as given as input to this \n",
    "        function. For example, if one word here is \"Hi\", then the regex \n",
    "        produced by this function will not catch \"hi\".\n",
    "        \n",
    "        If false, will return a regex string that will only work if all letters\n",
    "        in search string are lowercase.\n",
    "        \n",
    "        The default is True.\n",
    "     \n",
    "    Warning\n",
    "    -------\n",
    "    See the last example. The regex is minimally greedy. \n",
    "    \n",
    "       \n",
    "    Feature Requests (participation credit available)\n",
    "    -------\n",
    "    1. A wrapper that takes the above inputs, the string to search, and a variable=count|text, and\n",
    "    returns either the number of hits or the text of the matching elements. (See the examples below.)\n",
    "    \n",
    "    2. Optionally clean the string before the regex stuff happens.\n",
    "    \n",
    "    3. Optionally ignore line breaks. \n",
    "    \n",
    "    4. Optionally make it lazy (in the last example, \n",
    "    the \"correct\" answer is probably 2, but it gives 1.)\n",
    "    \n",
    "        \n",
    "    Unsure about speed\n",
    "    -------\n",
    "    I don't think this is a very \"fast\" function, but it should be robust. \n",
    "  \n",
    "    \n",
    "    Suggested use\n",
    "    -------\n",
    "    # clean your starting string \n",
    "    a_string_you_have = 'jack and jill went up the hill'\n",
    "    \n",
    "    # 1. define words and set up the regex\n",
    "    words = ['jack','hill']                         \n",
    "    rgx = NEAR_regex(words)                       \n",
    "    \n",
    "    # 2a. count the number of times the word groups are in the text near each other\n",
    "    count = len(re.findall(rgx,a_string_you_have))              \n",
    "    print(count)  \n",
    "    \n",
    "    # 2b. print the actual text matches <-- great for checking!\n",
    "    text_of_matches = [m.group(0) for m in re.finditer(rgx,a_string_you_have)]\n",
    "    print(text_of_matches)\n",
    "\n",
    "    \n",
    "    Returns\n",
    "    -------\n",
    "    A string which is a regex that can be used to look for cases where all the \n",
    "    input words are near each other.\n",
    "\n",
    "    '''\n",
    "               \n",
    "    from itertools import permutations\n",
    "    \n",
    "    start = r'(?:\\b' # the r means \"raw\" as in the backslash is just a backslash, not an escape character\n",
    "    \n",
    "    if partial:\n",
    "        gap   = r'[A-Za-z]*\\b(?: +[^ \\n\\r]*){0,' +str(max_words_between)+r'} *\\b'\n",
    "        end   = r'[A-Za-z]*\\b)'\n",
    "    else:\n",
    "        gap   = r'\\b(?: +[^ \\n]*){0,' +str(max_words_between)+r'} *\\b'\n",
    "        end   = r'\\b)'\n",
    "        \n",
    "    regex_list = []\n",
    "    \n",
    "    for permu in list(permutations(list_of_words)):\n",
    "        # catch this permutation: start + word + gap (+ word + gap)... + end\n",
    "        if cases_matter: # case sensitive - what cases the user gives are given back\n",
    "              regex_list.append(start+gap.join(permu)+end)           \n",
    "        else: # the resulting search will only work if all words are lowercase\n",
    "            lowerpermu = [w.lower() for w in permu]\n",
    "            regex_list.append(start+gap.join(lowerpermu)+end)\n",
    "    \n",
    "    return '|'.join(regex_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a919594-684a-43c3-bd30-af40bdd61603",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
